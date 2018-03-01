from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from time import strftime, localtime
from datetime import date, time
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

import bcrypt

from models import *

# dog_alert = [] becomes a no-duplicate list of dogs who need vetting that day
def dog_alert():
    dog_alert = []
    dateToday = date.today()

    
    vac = VaccineDog.objects.filter(vaccine_due__lte=dateToday).order_by('dog__name')
    for x in range (0, len(vac)):
        if vac[x].dog not in dog_alert:
            dog_alert.append(vac[x].dog)

    prv = PreventionDog.objects.filter(prevention_due__lte=dateToday).order_by('dog__name')
    for x in range (0, len(prv)):
        if prv[x].dog not in dog_alert:
            dog_alert.append(prv[x].dog)
    
    tst = TestDog.objects.filter(test_due__lte=dateToday).order_by('dog__name')
    for x in range (0, len(tst)):
        if tst[x].dog not in dog_alert:
            dog_alert.append(tst[x].dog)

    return dog_alert

# cat_alert = [] becomes a no-duplicate list of cats who need vetting that day
def cat_alert():
    cat_alert = []
    dateToday = date.today()

    vac = VaccineCat.objects.filter(vaccine_due__lte=dateToday).order_by('cat__name')
    for x in range (0, len(vac)):
        if vac[x].cat not in cat_alert:
            cat_alert.append(vac[x].cat)

    prv = PreventionCat.objects.filter(prevention_due__lte=dateToday).order_by('cat__name')
    for x in range (0, len(prv)):
        if prv[x].cat not in cat_alert:
            cat_alert.append(prv[x].cat)

    tst = TestCat.objects.filter(test_due__lte=dateToday).order_by('cat__name')
    for x in range (0, len(tst)):
        if tst[x].cat not in cat_alert:
            cat_alert.append(tst[x].cat)
    
    return cat_alert


def index(request):
    if 'user_id' in request.session:
        dog_alert()
        cat_alert()
        dateToday = date.today()

        context = {
            "avail_dogs" : Dog.objects.exclude(adopted=True).order_by('name'),
            "avail_cats" : Cat.objects.exclude(adopted=True).order_by('name'),
            
            "dog_alert" : dog_alert,
            "cat_alert" : cat_alert,
           
            "date_today" : dateToday
        }
        return render(request, 'resQmia_app/dashboard_new_dog.html', context)
    else:
        return render(request, 'resQmia_app/index.html')

def dashboard(request):
    if 'user_id' in request.session:
        return render(request, 'resQmia_app/dashboard_dog.html')
    else:
        return render(request, 'resQmia_app/index.html')

def register(request):

    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.add_message(request, messages.ERROR, errors[tag])
        return redirect('resQmia_app:login')
    else:
        first_name =  request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
 
        user = User.objects.create_user(first_name, last_name, email, hashed_password)

        if not user:
            messages.add_message(request, messages.ERROR, "User exists, please login.")
            return redirect('login_reg_app_login')
        else:
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['email'] = user.email
            return redirect('/dashboard')
        
def login(request):
    try:
        user = User.objects.login_validator(request.POST)

        if user:
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['email'] = user.email
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, "Invalid login info.")
            return redirect("/")
    except:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')


def new_dog(request):
    dog_alert()
    cat_alert()
    dateToday = date.today()

    context = {

        "avail_dogs" : Dog.objects.exclude(adopted=True).order_by('name'),
        "avail_cats" : Cat.objects.exclude(adopted=True).order_by('name'),
        "dog_alert" : dog_alert,
        "cat_alert" : cat_alert,
        "date_today" : dateToday
    }
    return render(request, 'resQmia_app/dashboard_new_dog.html', context)

def rescue_dog(request):
    dateToday = date.today()
    if request.method == 'POST':
        name = request.POST['name'].capitalize()
        rescue_date = request.POST['rescue_date']
        source = request.POST['source']
        source_note = request.POST['source_note']
        microchip_number = 0
        if 'microchip' in request.POST:
            microchip_number = request.POST['microchip_number']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        description = request.POST['description']
        weight = request.POST['weight']

        thumb = "../media/default.jpg"
        if 'picture' in request.POST:
            thumb=request.FILES['thumb']
            
        fixed = False
        if 'fixed' in request.POST:
            fixed = True

        adopted = False

        d = Dog.objects.create(name=name, rescue_date=rescue_date, source=source, source_note=source_note,  microchip_number=microchip_number, birthdate=birthdate, gender=gender, description=description, weight=weight, fixed=fixed, adopted=adopted, thumb=thumb)        

        # ************************    VACCINATIONS
        
        rv = VaccineDog.objects.create(vaccine_name="rabies", vaccine_due=dateToday, dog_id=d.id)
        dv = VaccineDog.objects.create(vaccine_name="da2pp", vaccine_due=dateToday, dog_id=d.id)
        lv = VaccineDog.objects.create(vaccine_name="lepto", vaccine_due=dateToday, dog_id=d.id)
        bv = VaccineDog.objects.create(vaccine_name="bord", vaccine_due=dateToday, dog_id=d.id)
        cv = VaccineDog.objects.create(vaccine_name="civ", vaccine_due=dateToday, dog_id=d.id)

        # ************************    PREVENTIONS

        hwp = PreventionDog.objects.create(prevention_name="heartworm", prevention_due=dateToday, dog_id=d.id)
        ftp = PreventionDog.objects.create(prevention_name="flea", prevention_due=dateToday, dog_id=d.id)
        
        # ************************    TESTS

        hwt = TestDog.objects.create(test_name="heartworm", test_due=dateToday, dog_id=d.id)
        fft = TestDog.objects.create(test_name="fecal", test_due=dateToday, dog_id=d.id)
        dwt = TestDog.objects.create(test_name="dewormer", test_due=dateToday, dog_id=d.id)
        

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def select_our_dogs(request, dog_id):
    dateToday = date.today()
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="rabies")
    current_da2pp = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="da2pp")
    current_lepto = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="flea")
    current_heartworm_test = TestDog.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = TestDog.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = TestDog.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
    avail_dogs = Dog.objects.exclude(adopted=True).order_by('name')
    avail_cats = Cat.objects.exclude(adopted=True).order_by('name')

    context = {
        'current_dog' : current_dog,
        'current_rabies' : current_rabies,
        'current_da2pp' : current_da2pp,
        'current_lepto' : current_lepto,
        'current_bord' : current_bord,
        'current_civ' : current_civ,
        'current_heartworm_prev' : current_heartworm_prev,
        'current_flea_tick' : current_flea_tick,
        'current_heartworm_test' : current_heartworm_test,
        'current_fecal' : current_fecal,
        'current_dewormer' : current_dewormer,

        'avail_dogs' : avail_dogs,
        'avail_cats' : avail_cats,

        'date_today' : dateToday,
    }
    
    return render(request, 'resQmia_app/our_dogs.html', context)

def select_dashboard(request, dog_id):
    
    dateToday = date.today()
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="rabies")
    current_da2pp = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="da2pp")
    current_lepto = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="flea")
    current_heartworm_test = TestDog.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = TestDog.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = TestDog.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
    avail_dogs = Dog.objects.exclude(adopted=True).order_by('name')
    avail_cats = Cat.objects.exclude(adopted=True).order_by('name')

    context = {
        'current_dog' : current_dog,
        'current_rabies' : current_rabies,
        'current_da2pp' : current_da2pp,
        'current_lepto' : current_lepto,
        'current_bord' : current_bord,
        'current_civ' : current_civ,
        'dog_alert' : dog_alert,
        'cat_alert' : cat_alert,
        'current_heartworm_prev' : current_heartworm_prev,
        'current_flea_tick' : current_flea_tick,
        'current_heartworm_test' : current_heartworm_test,
        'current_fecal' : current_fecal,
        'current_dewormer' : current_dewormer,

        'avail_dogs' : avail_dogs,
        'avail_cats' : avail_cats,

        'date_today' : dateToday,

    }
    
    return render(request, 'resQmia_app/dashboard_dog.html', context)


def select_our_dogs(request, dog_id):
    dateToday = date.today()
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="rabies")
    current_da2pp = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="da2pp")
    current_lepto = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="flea")
    current_heartworm_test = TestDog.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = TestDog.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = TestDog.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
    avail_dogs = Dog.objects.exclude(adopted=True).order_by('name')
    avail_cats = Cat.objects.exclude(adopted=True).order_by('name')

    context = {
        'current_dog' : current_dog,
        'current_rabies' : current_rabies,
        'current_da2pp' : current_da2pp,
        'current_lepto' : current_lepto,
        'current_bord' : current_bord,
        'current_civ' : current_civ,
        'current_heartworm_prev' : current_heartworm_prev,
        'current_flea_tick' : current_flea_tick,
        'current_heartworm_test' : current_heartworm_test,
        'current_fecal' : current_fecal,
        'current_dewormer' : current_dewormer,

        'avail_dogs' : avail_dogs,
        'avail_cats' : avail_cats,

        'date_today' : dateToday,

    }
    
    return render(request, 'resQmia_app/our_dogs.html', context)

def delete_dog(request, dog_id):
    dog = Dog.objects.filter(id=dog_id)
    dog.delete()
    
    return redirect('/our_dogs')

def select_day(request, dog_id):
    dateToday = date.today()

    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = VaccineDog.objects.filter(dog_id=dog_id)
    current_da2pp = VaccineDog.objects.filter(dog_id=dog_id)
    current_lepto = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="flea")
    current_heartworm_test = TestDog.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = TestDog.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = TestDog.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
    avail_dogs = Dog.objects.exclude(adopted=True).order_by('name')
    avail_cats = Cat.objects.exclude(adopted=True).order_by('name')

    context = {
        'current_dog' : current_dog,
        'current_rabies' : current_rabies,
        'current_da2pp' : current_da2pp,
        'current_lepto' : current_lepto,
        'current_bord' : current_bord,
        'current_civ' : current_civ,
        'current_heartworm_prev' : current_heartworm_prev,
        'current_flea_tick' : current_flea_tick,
        'current_heartworm_test' : current_heartworm_test,
        'current_fecal' : current_fecal,
        'current_dewormer' : current_dewormer,

        'avail_dogs' : avail_dogs,
        'avail_cats' : avail_cats,

        'date_today' : dateToday,
    }
    
    return render(request, 'resQmia_app/dashboard_dog.html', context)

def select_adopted(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    adopted_dogs = Dog.objects.filter(adopted=True)
   
    print current_dog
   
    context = {
        "adopted_dogs" : adopted_dogs,
        'current_dog' : current_dog,
    }
    
    return render(request, 'resQmia_app/adopted.html', context)

def adopted(request, dog_id):
    adopted_dog = Dog.objects.get(id=dog_id)
    adopted_dog.adopted = True
    adopted_dog.save()

    return redirect('/')

def adopted_dogs(request):
    adopted_dogs = Dog.objects.filter(adopted=True)
    context = {
        'adopted_dogs' : adopted_dogs
    }

    return render(request, 'resQmia_app/adopted.html', context)

def our_dogs(request):
    avail_dogs = Dog.objects.exclude(adopted=True).order_by('name')

    context = {
        "avail_dogs" : avail_dogs,
    }
    print avail_dogs
    return render(request, 'resQmia_app/dashboard_dog.html', context)




def new_vaccine_dog(request, id):
    if request.method == 'POST':
        
        current_record = VaccineDog.objects.get(id=id)
        
        current_record.vaccine_given = request.POST['vaccine_given']
        current_record.vaccine_due = request.POST['vaccine_due']
        current_record.vaccine_number = request.POST['vaccine_number']

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def new_prevention_dog(request, id):
    if request.method == 'POST':
        
        current_record = PreventionDog.objects.get(id=id)
        
        current_record.prevention_given = request.POST['prevention_given']
        current_record.prevention_due = request.POST['prevention_due']

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def new_test_dog(request, id):
    if request.method == 'POST':
    
        current_record = TestDog.objects.get(id=id)
    
        current_record.test_given = request.POST['test_given']
        current_record.test_due = request.POST['test_due']

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def fix(request, dog_id):
    if request.method == 'POST':
        
        current_record = Dog.objects.get(id=dog_id)

        current_record.fixed = True

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def microchip(request, dog_id):
    if request.method == 'POST':
        
        current_record = Dog.objects.get(id=dog_id)

        current_record.microchip_number = request.POST['microchip_number']

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # CATS!!!!!!!!!!!!!! =============================================================



def delete_cat(request, cat_id):
    cat = Cat.objects.filter(id=cat_id)
    cat.delete()

    return redirect('/our_cats')



def our_cats(request):
    avail_cats = Cat.objects.exclude(adopted=True).order_by('name')

    context = {
        "avail_cats" : avail_cats,
    }
    return render(request, 'resQmia_app/our_cats.html', context)    

def new_cat(request):
    dog_alert()
    cat_alert()
    dateToday = date.today()

    avail_cats = Cat.objects.exclude(adopted=True).order_by('name')
    avail_dogs = Dog.objects.exclude(adopted=True).order_by('name')

    context = {
    
        'dog_alert' : dog_alert,
        'cat_alert' : cat_alert,
        'avail_cats' : avail_cats,
        'avail_dogs' : avail_dogs,

        'date_today' : dateToday,

    }
    
    return render(request, 'resQmia_app/dashboard_new_cat.html', context)

def rescue_cat(request):
    dateToday = date.today()
    if request.method == 'POST':
        name = request.POST['name']
        rescue_date = request.POST['rescue_date']
        source = request.POST['source']
        source_note = request.POST['source_note']
        microchip_number = 0
        if 'microchip' in request.POST:
            microchip_number = request.POST['microchip_number']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        description = request.POST['description']
        weight = request.POST['weight']
        thumb = request.FILES['thumb']
        fixed = False
        if 'fixed' in request.POST:
            fixed = True
        adopted = False
        d = Cat.objects.create(name=name, rescue_date=rescue_date, source=source, source_note=source_note, microchip_number=microchip_number, birthdate=birthdate, gender=gender, description=description, weight=weight, thumb=thumb, fixed=fixed, adopted=adopted)

        # ************************    VACCINATIONS

        rv = VaccineCat.objects.create(vaccine_name="rabies", vaccine_due=dateToday, cat_id=d.id)
        fv = VaccineCat.objects.create(vaccine_name="fvrcp", vaccine_due=dateToday, cat_id=d.id)

        # ************************    PREVENTIONS

        ftp = PreventionCat.objects.create(prevention_name="flea", prevention_due=dateToday, cat_id=d.id)
        rvp = PreventionCat.objects.create(prevention_name="revolution", prevention_due=dateToday, cat_id=d.id)

        # ************************    TESTS

        fiv = TestCat.objects.create(test_name="fivfelv", test_due=dateToday, cat_id=d.id)
        fcl = TestCat.objects.create(test_name="fecal", test_due=dateToday, cat_id=d.id)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def select_our_cats(request, cat_id):
    dateToday = date.today()
    current_cat = Cat.objects.filter(id=cat_id)
    current_rabies = VaccineCat.objects.filter(cat_id=cat_id, vaccine_name="rabies")
    current_fvrcp = VaccineCat.objects.filter(cat_id=cat_id, vaccine_name="fvrcp")
    current_flea = PreventionCat.objects.filter(cat_id=cat_id, prevention_name="flea")
    current_revolution = PreventionCat.objects.filter(cat_id=cat_id, prevention_name="revolution")        
    current_fivfelv = TestCat.objects.filter(cat_id=cat_id, test_name="fivfelv")
    current_fecal = TestCat.objects.filter(cat_id=cat_id, test_name="fecal")
    
    avail_cats = Cat.objects.exclude(adopted=True).order_by('name')
    avail_dogs = Dog.objects.exclude(adopted=True).order_by('name')

    context = {
        'current_cat' : current_cat,
        'current_rabies' : current_rabies,
        'current_fvrcp' : current_fvrcp,
        'current_flea' : current_flea,
        'current_revolution' : current_revolution,
        'current_fivfelv' : current_fivfelv,
        'current_fecal' : current_fecal,

        'avail_cats' : avail_cats,
        'avail_dogs' : avail_dogs,

        'date_today' : dateToday,

    }
    
    return render(request, 'resQmia_app/our_cats.html', context)



def new_vaccine_cat(request, id):
    if request.method == 'POST':
        
        current_record = VaccineCat.objects.get(id=id)
        
        current_record.vaccine_given = request.POST['vaccine_given']
        current_record.vaccine_due = request.POST['vaccine_due']
        current_record.vaccine_number = request.POST['vaccine_number']

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def new_prevention_cat(request, id):
    if request.method == 'POST':
        
        current_record = PreventionCat.objects.get(id=id)
        
        current_record.prevention_given = request.POST['prevention_given']
        current_record.prevention_due = request.POST['prevention_due']

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def new_test_cat(request, id):
    if request.method == 'POST':
    
        current_record = TestCat.objects.get(id=id)
    
        current_record.test_given = request.POST['test_given']
        current_record.test_due = request.POST['test_due']

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def select_dashboard_cat(request, cat_id):
    
    dateToday = date.today()

    current_cat = Cat.objects.filter(id=cat_id)
    current_rabies = VaccineCat.objects.filter(cat_id=cat_id, vaccine_name="rabies")
    current_fvrcp = VaccineCat.objects.filter(cat_id=cat_id, vaccine_name="fvrcp")
    current_flea = PreventionCat.objects.filter(cat_id=cat_id, prevention_name="flea")
    current_revolution = PreventionCat.objects.filter(cat_id=cat_id, prevention_name="revolution")
    current_fivfelv = TestCat.objects.filter(cat_id=cat_id, test_name="fivfelv")
    current_fecal = TestCat.objects.filter(cat_id=cat_id, test_name="fecal")
    
    avail_cats = Cat.objects.exclude(adopted=True).order_by('name')
    avail_dogs = Dog.objects.exclude(adopted=True).order_by('name')

    context = {
        'current_cat' : current_cat,
        'cat_alert' : cat_alert,
        'dog_alert' : dog_alert,
        'current_rabies' : current_rabies,
        'current_fvrcp' : current_fvrcp,
        'current_flea' : current_flea,
        'current_revolution' : current_revolution,
        'current_fivfelv' : current_fivfelv,
        'current_fecal' : current_fecal,

        'avail_cats' : avail_cats,
        'avail_dogs' : avail_dogs,

        'date_today' : dateToday,

    }
    
    return render(request, 'resQmia_app/dashboard_cat.html', context)




def fix_cat(request, cat_id):
    if request.method == 'POST':
    
        current_record = Cat.objects.get(id=cat_id)

        current_record.fixed = True

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def microchip_cat(request, cat_id):
    if request.method == 'POST':
        
        current_record = Cat.objects.get(id=cat_id)

        current_record.microchip_number = request.POST['microchip_number']

        current_record.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


