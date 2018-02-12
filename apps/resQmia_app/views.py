from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
from datetime import date, time
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

from models import *

dateToday = date.today()
print "*****"
print "TODAY IS: ", dateToday
print "*****"

# dog_alert = [] becomes a no-duplicate list of dogs who need vetting that day
def dog_alert():
    dog_alert = []

    rbv = VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="rabies").order_by('vaccine_due')
    for x in range (0, len(rbv)):
        print rbv[x].dog
        dog_alert.append(rbv[x].dog)
    dav = VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="da2pp").order_by('vaccine_due')
    for x in range (0, len(dav)):
        if dav[x].dog not in dog_alert:
            dog_alert.append(dav[x].dog)
    lpv = VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="lepto").order_by('vaccine_due')
    for x in range (0, len(lpv)):
        if lpv[x].dog not in dog_alert:
            dog_alert.append(lpv[x].dog)
    bdv = VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="bord").order_by('vaccine_due')
    for x in range (0, len(bdv)):
        if bdv[x].dog not in dog_alert:
            dog_alert.append(bdv[x].dog)
    civ = VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="civ").order_by('vaccine_due')
    for x in range (0, len(civ)):
        if civ[x].dog not in dog_alert:
            dog_alert.append(civ[x].dog)

    hwp = PreventionDog.objects.filter(prevention_due__lte=dateToday, prevention_name="heartworm").order_by('prevention_due')
    for x in range (0, len(hwp)):
        if hwp[x].dog not in dog_alert:
            dog_alert.append(hwp[x].dog)
    ftp = PreventionDog.objects.filter(prevention_due__lte=dateToday, prevention_name="fleaTick").order_by('prevention_due')
    for x in range (0, len(ftp)):
        if ftp[x].dog not in dog_alert:
            dog_alert.append(ftp[x].dog)
    hwt = PreventionDog.objects.filter(prevention_due__lte=dateToday, prevention_name="heartworm").order_by('prevention_due')
    for x in range (0, len(hwt)):
        if hwt[x].dog not in dog_alert:
            dog_alert.append(hwt[x].dog)
    fct = TestDog.objects.filter(test_due__lte=dateToday, test_name="fecal").order_by('test_due')
    for x in range (0, len(fct)):
        if fct[x].dog not in dog_alert:
            dog_alert.append(fct[x].dog)
    dwd = TestDog.objects.filter(test_due__lte=dateToday, test_name="dewormer").order_by('test_due')
    for x in range (0, len(dwd)):
        if dwd[x].dog not in dog_alert:
            dog_alert.append(dwd[x].dog)

    return dog_alert


# cat_alert = [] becomes a no-duplicate list of cats who need vetting that day
def cat_alert():
    cat_alert = []

    rbv = VaccineCat.objects.filter(vaccine_due__lte=dateToday, vaccine_name="rabies").order_by('vaccine_due')
    for x in range (0, len(rbv)):
        print rbv[x].cat
        cat_alert.append(rbv[x].cat)
    dav = VaccineCat.objects.filter(vaccine_due__lte=dateToday, vaccine_name="da2pp").order_by('vaccine_due')
    for x in range (0, len(dav)):
        if dav[x].cat not in cat_alert:
            cat_alert.append(dav[x].cat)
    lpv = VaccineCat.objects.filter(vaccine_due__lte=dateToday, vaccine_name="lepto").order_by('vaccine_due')
    for x in range (0, len(lpv)):
        if lpv[x].cat not in cat_alert:
            cat_alert.append(lpv[x].cat)
    bdv = VaccineCat.objects.filter(vaccine_due__lte=dateToday, vaccine_name="bord").order_by('vaccine_due')
    for x in range (0, len(bdv)):
        if bdv[x].cat not in cat_alert:
            cat_alert.append(bdv[x].cat)
    civ = VaccineCat.objects.filter(vaccine_due__lte=dateToday, vaccine_name="civ").order_by('vaccine_due')
    for x in range (0, len(civ)):
        if civ[x].cat not in cat_alert:
            cat_alert.append(civ[x].cat)

    hwp = PreventionDog.objects.filter(prevention_due__lte=dateToday, prevention_name="heartworm").order_by('prevention_due')
    for x in range (0, len(hwp)):
        if hwp[x].cat not in cat_alert:
            cat_alert.append(hwp[x].cat)
    ftp = PreventionDog.objects.filter(prevention_due__lte=dateToday, prevention_name="fleaTick").order_by('prevention_due')
    for x in range (0, len(ftp)):
        if ftp[x].cat not in cat_alert:
            cat_alert.append(ftp[x].cat)
    hwt = PreventionDog.objects.filter(prevention_due__lte=dateToday, prevention_name="heartworm").order_by('prevention_due')
    for x in range (0, len(hwt)):
        if hwt[x].cat not in cat_alert:
            cat_alert.append(hwt[x].cat)
    fct = TestDog.objects.filter(test_due__lte=dateToday, test_name="fecal").order_by('test_due')
    for x in range (0, len(fct)):
        if fct[x].cat not in cat_alert:
            cat_alert.append(fct[x].cat)
    dwd = TestDog.objects.filter(test_due__lte=dateToday, test_name="dewormer").order_by('test_due')
    for x in range (0, len(dwd)):
        if dwd[x].cat not in cat_alert:
            cat_alert.append(dwd[x].cat)

    return cat_alert


def index(request):
    if 'user_id' in request.session:
        dog_alert()
        # cat_alert()

        context = {
        "avail_dogs" : Dog.objects.exclude(adopted=True),
        "rabies" : VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="rabies").order_by('vaccine_due'),
        "da2pp" : VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="da2pp").order_by('vaccine_due'),
        "lepto" : VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="lepto").order_by('vaccine_due'),
        "bord" : VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="bord").order_by('vaccine_due'),
        "civs" : VaccineDog.objects.filter(vaccine_due__lte=dateToday, vaccine_name="civ").order_by('vaccine_due'),
        "dog_alert" : dog_alert,
        "heartwormPrev" : PreventionDog.objects.filter(prevention_due__lte=dateToday).order_by('prevention_due'),
        "fleaTick" : PreventionDog.objects.filter(prevention_due__lte=dateToday).order_by('prevention_due'),
        "heartwormTestDog" : TestDog.objects.filter(test_due__lte=dateToday).order_by('test_due'),
        "fecalTestDog" : TestDog.objects.filter(test_due__lte=dateToday).order_by('test_due'),
        "dewormer" : TestDog.objects.filter(test_due__lte=dateToday).order_by('test_due')
        }
        return render(request, 'resQmia_app/dashboard.html', context)
    else:
        return render(request, 'resQmia_app/index.html')

def dashboard(request):
    if 'user_id' in request.session:
        return render(request, 'resQmia_app/dashboard.html')
    else:
        return render(request, 'resQmia_app/index.html')

def register(request):

    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.add_message(request, messages.ERROR, errors[tag])
        return redirect('login_app:login')
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
    return render(request, 'resQmia_app/new_dog.html')

def rescue_dog(request):
    dateToday = date.today()
    if request.method == 'POST':
        name = request.POST['name']
        microchip_number = 0
        if 'microchip' in request.POST:
            microchip_number = request.POST['microchip_number']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        description = request.POST['description']
        weight = request.POST['weight']
        fixed = False
        if 'fixed' in request.POST:
            fixed = True
        adopted = False
        d = Dog.objects.create(name=name, microchip_number=microchip_number, birthdate=birthdate, gender=gender, description=description, weight=weight, fixed=fixed, adopted=adopted)

        # ************************    VACCINATIONS
        rabies = request.POST['rabiesVac']
        if rabies == "False":
            rabies_due = request.POST['rabies_due']
            rv = VaccineDog.objects.create(vaccine_name="rabies", vaccine_due=rabies_due, dog_id=d.id)

        elif rabies == "True":
            rabies_given = request.POST['rabies_given']
            rabies_due = request.POST['rabies_due']
            rabies_number = request.POST['rabies_number']
            rv = VaccineDog.objects.create(vaccine_name="rabies", vaccine_given=rabies_given, vaccine_due=rabies_due, vaccine_number=rabies_number, dog_id=d.id)

        da2pp = request.POST['da2ppVac']
        if da2pp == "False":
            da2pp_due = dateToday
            da2pp_given = '1999-01-01'
            
        elif da2pp == "True":
            da2pp_given = request.POST['da2pp_given']
            da2pp_due = request.POST['da2pp_due']
        dv = VaccineDog.objects.create(vaccine_name="da2pp", vaccine_given=da2pp_given, vaccine_due=da2pp_due, dog_id=d.id)

        lepto = request.POST['leptoVac']
        if lepto == "False":
            lepto_due = dateToday
            lepto_given = '1999-01-01'
        
        elif lepto == "True":
            lepto_given = request.POST['leptoGiven']
            lepto_due = request.POST['leptoDue']
        lv = VaccineDog.objects.create(vaccine_name="lepto", vaccine_given=lepto_given, vaccine_due=lepto_due, dog_id=d.id)

        bord = request.POST['bordVac']
        if bord == "False":
            bord_due = dateToday
            bord_given = '1999-01-01'

        elif bord == "True":    
            bord_given = request.POST['bordGiven']
            bord_due = request.POST['bordDue']
        bv = VaccineDog.objects.create(vaccine_name="bord", vaccine_given=bord_given, vaccine_due=bord_due, dog_id=d.id)

        civ = request.POST['civVac']
        if civ == "False":
            civ_due = dateToday
            civ_given = '1999-01-01'

        elif civ == "True":
            civ_given = request.POST['civGiven']
            civ_due = request.POST['civDue']    
        cv = VaccineDog.objects.create(vaccine_name="civ", vaccine_given=civ_given, vaccine_due=civ_due, dog_id=d.id)

        # ************************    PREVENTIONS

        heartworm_prev_due = request.POST['heartwormPrevDue']
        hwp = PreventionDog.objects.create(prevention_name="heartworm", prevention_due=heartworm_prev_due, dog_id=d.id)

        flea_tick_due = request.POST['fleaPrevDue']
        ftp = PreventionDog.objects.create(prevention_name="fleaTick", prevention_due=flea_tick_due, dog_id=d.id)

        heartworm_test_due = request.POST['heartwormTestDue']
        hwt = TestDog.objects.create(test_name="heartworm", test_due=heartworm_test_due, dog_id=d.id)

        fecal_test_due = request.POST['fecalTestDue']
        fft = TestDog.objects.create(test_name="fecal", test_due=fecal_test_due, dog_id=d.id)

        dewormer_due = request.POST['dewormerTestDue']
        dwt = TestDog.objects.create(test_name="dewormer", test_due=dewormer_due, dog_id=d.id)
        

    return redirect ('/our_dogs')


def select_our_dogs(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="rabies")
    current_da2pp = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="da2pp")
    current_lepto = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="fleaTick")
    current_heartworm_test = TestDog.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = TestDog.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = TestDog.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
    avail_dogs = Dog.objects.exclude(adopted=True)

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

    }
    
    return render(request, 'resQmia_app/our_dogs.html', context)

def select_dashboard(request, dog_id):
    
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="rabies")
    current_da2pp = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="da2pp")
    current_lepto = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="fleaTick")
    current_heartworm_test = TestDog.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = TestDog.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = TestDog.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
    avail_dogs = Dog.objects.exclude(adopted=True)

    context = {
        'current_dog' : current_dog,
        'current_rabies' : current_rabies,
        'current_da2pp' : current_da2pp,
        'current_lepto' : current_lepto,
        'current_bord' : current_bord,
        'current_civ' : current_civ,
        'dog_alert' : dog_alert,
        'current_heartworm_prev' : current_heartworm_prev,
        'current_flea_tick' : current_flea_tick,
        'current_heartworm_test' : current_heartworm_test,
        'current_fecal' : current_fecal,
        'current_dewormer' : current_dewormer,

        'avail_dogs' : avail_dogs,

    }
    
    return render(request, 'resQmia_app/dashboard.html', context)


def select_our_dogs(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="rabies")
    current_da2pp = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="da2pp")
    current_lepto = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="fleaTick")
    current_heartworm_test = TestDog.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = TestDog.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = TestDog.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
    avail_dogs = Dog.objects.exclude(adopted=True)

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

    }
    
    return render(request, 'resQmia_app/our_dogs.html', context)

def delete_dog(request, dog_id):
    dog = Dog.objects.filter(id=dog_id)
    dog.delete()
    
    return redirect('/our_dogs')

def select_day(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = VaccineDog.objects.filter(dog_id=dog_id)
    current_da2pp = VaccineDog.objects.filter(dog_id=dog_id)
    current_lepto = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = VaccineDog.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = PreventionDog.objects.filter(dog_id=dog_id, prevention_name="fleaTick")
    current_heartworm_test = TestDog.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = TestDog.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = TestDog.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
    avail_dogs = Dog.objects.exclude(adopted=True)

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

    }
    
    return render(request, 'resQmia_app/dashboard.html', context)

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
    avail_dogs = Dog.objects.exclude(adopted=True)

    context = {
        "avail_dogs" : avail_dogs,
    }
    print avail_dogs
    return render(request, 'resQmia_app/our_dogs.html', context)




def new_vaccine_dog(request, id):
    if request.method == 'POST':
        
        current_record = VaccineDog.objects.get(id=id)
        
        current_record.vaccine_given = request.POST['vaccine_given']
        current_record.vaccine_due = request.POST['vaccine_due']
        current_record.vaccine_number = request.POST['vaccine_number']

        current_record.save()

    return redirect('/')


def new_prevention_dog(request, id):
    if request.method == 'POST':
        
        current_record = PreventionDog.objects.get(id=id)
        
        current_record.prevention_given = request.POST['prevention_given']
        current_record.prevention_due = request.POST['prevention_due']

        current_record.save()

    return redirect('/')


def new_test_dog(request, id):
    if request.method == 'POST':
    
        current_record = TestDog.objects.get(id=id)
    
        current_record.test_given = request.POST['test_given']
        current_record.test_due = request.POST['test_due']

        current_record.save()

    return redirect('/')

    # CATS!!!!!!!!!!!!!! =============================================================



def delete_cat(request, cat_id):
    cat = Cat.objects.filter(id=cat_id)
    cat.delete()

    return redirect('/our_cats')



def our_cats(request):
    avail_cats = Cat.objects.exclude(adopted=True)

    context = {
        "avail_cats" : avail_cats,
    }
    print avail_cats
    return render(request, 'resQmia_app/our_cats.html', context)    

def new_cat(request):
    return render(request, 'resQmia_app/new_cat.html')

def rescue_cat(request):
    dateToday = date.today()
    if request.method == 'POST':
        name = request.POST['name']
        microchip_number = 0
        if 'microchip' in request.POST:
            microchip_number = request.POST['microchip_number']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        description = request.POST['description']
        weight = request.POST['weight']
        fixed = False
        if 'fixed' in request.POST:
            fixed = True
        adopted = False
        d = Cat.objects.create(name=name, microchip_number=microchip_number, birthdate=birthdate, gender=gender, description=description, weight=weight, fixed=fixed, adopted=adopted)

        # ************************    VACCINATIONS
        rabies = request.POST['rabiesVac']
        if rabies == "False":
            rabies_due = request.POST['rabies_due']
            rv = VaccineCat.objects.create(vaccine_name="rabies", vaccine_due=rabies_due, cat_id=d.id)

        elif rabies == "True":
            rabies_given = request.POST['rabies_given']
            rabies_due = request.POST['rabies_due']
            rabies_number = request.POST['rabies_number']
            rv = VaccineCat.objects.create(vaccine_name="rabies", vaccine_given=rabies_given, vaccine_due=rabies_due, vaccine_number=rabies_number, cat_id=d.id)

        fvrcp = request.POST['fvrcpVac']
        if fvrcp == "False":
            fvrcp_due = dateToday
            fvrcp_given = '1999-01-01'
            
        elif fvrcp == "True":
            fvrcp_given = request.POST['fvrcp_given']
            fvrcp_due = request.POST['fvrcp_due']
        dv = VaccineCat.objects.create(vaccine_name="fvrcp", vaccine_given=fvrcp_given, vaccine_due=fvrcp_due, cat_id=d.id)

        # ************************    PREVENTIONS

        flea_tick_due = request.POST['fleaPrevDue']
        ftp = PreventionCat.objects.create(prevention_name="fleaTick", prevention_due=flea_tick_due, cat_id=d.id)

        revolution_prev_due = request.POST['revolutionPrevDue']
        rvp = PreventionCat.objects.create(prevention_name="revolution", prevention_due=revolution_prev_due, cat_id=d.id)

        fivfelv_due = request.POST['fivfelvTestDue']
        fft = TestCat.objects.create(test_name="fivfelv", test_due=fivfelv_due, cat_id=d.id)

        fecal_test_due = request.POST['fecalTestDue']
        fft = TestCat.objects.create(test_name="fecal", test_due=fecal_test_due, cat_id=d.id)

        
        
    return redirect ('/our_cats')

def select_our_cats(request, cat_id):
    current_cat = Cat.objects.filter(id=cat_id)
    current_rabies = VaccineCat.objects.filter(cat_id=cat_id, vaccine_name="rabies")
    current_fvrcp = VaccineCat.objects.filter(cat_id=cat_id, vaccine_name="fvrcp")
    current_flea = PreventionCat.objects.filter(cat_id=cat_id, prevention_name="fleaTick")
    current_revolution = PreventionCat.objects.filter(cat_id=cat_id, prevention_name="revolution")        
    current_fivfelv = TestCat.objects.filter(cat_id=cat_id, test_name="fivfelv")
    current_fecal = TestCat.objects.filter(cat_id=cat_id, test_name="fecal")
    
    avail_cats = Cat.objects.exclude(adopted=True)

    context = {
        'current_cat' : current_cat,
        'current_rabies' : current_rabies,
        'current_fvrcp' : current_fvrcp,
        'current_flea' : current_flea,
        'current_revolution' : current_revolution,
        'current_fivfelv' : current_fivfelv,
        'current_fecal' : current_fecal,

        'avail_cats' : avail_cats,

    }
    
    return render(request, 'resQmia_app/our_cats.html', context)