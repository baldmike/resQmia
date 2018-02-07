from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime
from datetime import date, time
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

from models import *

today = date.today()
print "*****"
print "TODAY IS: ", today
print "*****"

def index(request):
    if 'user_id' in request.session:
        vaccines_due = []
        dateToday = date.today()
        print dateToday, "THIS THIS THIS"
        rbv = RabiesVaccine.objects.filter(vaccine_due__lte=dateToday).order_by('vaccine_due')
        for x in range (0, len(rbv)):
            print rbv[x].dog
            vaccines_due.append(rbv[x].dog)
        dav = Da2ppVaccine.objects.filter(vaccine_due__lte=dateToday).order_by('vaccine_due')
        for x in range (0, len(dav)):
            if dav[x].dog not in vaccines_due:
                vaccines_due.append(dav[x].dog)
        lpv = Vaccine.objects.filter(vaccine_due__lte=dateToday, vaccine_name="lepto").order_by('vaccine_due')
        for x in range (0, len(lpv)):
            if lpv[x].dog not in vaccines_due:
                vaccines_due.append(lpv[x].dog)
        bdv = Vaccine.objects.filter(vaccine_due__lte=dateToday, vaccine_name="bord").order_by('vaccine_due')
        for x in range (0, len(bdv)):
            if bdv[x].dog not in vaccines_due:
                vaccines_due.append(bdv[x].dog)
        civ = Vaccine.objects.filter(vaccine_due__lte=dateToday, vaccine_name="civ").order_by('vaccine_due')
        for x in range (0, len(civ)):
            if civ[x].dog not in vaccines_due:
                vaccines_due.append(civ[x].dog)

        print vaccines_due
        context = {
        "avail_dogs" : Dog.objects.exclude(adopted=True),
        "rabies" : RabiesVaccine.objects.filter(vaccine_due__lte=dateToday).order_by('vaccine_due'),
        "da2pp" : Da2ppVaccine.objects.filter(vaccine_due__lte=dateToday).order_by('vaccine_due'),
        "lepto" : Vaccine.objects.filter(vaccine_due__lte=dateToday, vaccine_name="lepto").order_by('vaccine_due'),
        "bord" : Vaccine.objects.filter(vaccine_due__lte=dateToday, vaccine_name="bord").order_by('vaccine_due'),
        "civs" : Vaccine.objects.filter(vaccine_due__lte=dateToday, vaccine_name="civ").order_by('vaccine_due'),
        "vaccines_due" : vaccines_due,
        "heartwormPrev" : Prevention.objects.filter(prevention_due__lte=dateToday).order_by('prevention_due'),
        "fleaTick" : Prevention.objects.filter(prevention_due__lte=dateToday).order_by('prevention_due'),
        "heartwormTest" : Test.objects.filter(test_due__lte=dateToday).order_by('test_due'),
        "fecalTest" : Test.objects.filter(test_due__lte=dateToday).order_by('test_due'),
        "dewormer" : Test.objects.filter(test_due__lte=dateToday).order_by('test_due')
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
            rabies_due = request.POST['rabiesDue']
            rv = RabiesVaccine.objects.create(vaccine_name="rabies", vaccine_due=rabies_due, dog_id=d.id)

        elif rabies == "True":
            rabies_given = request.POST['rabiesGiven']
            rabies_due = request.POST['rabiesDue']
            rabies_number = request.POST['rabiesNumber']
            rv = RabiesVaccine.objects.create(vaccine_name="rabies", vaccine_given=rabies_given, vaccine_due=rabies_due, vaccine_number=rabies_number, dog_id=d.id)

        da2pp = request.POST['da2ppVac']
        if da2pp == "False":
            da2pp_given = "1999-01-01"
            da2pp_due = today
            
        elif da2pp == "True":
            da2pp_given = request.POST['da2ppGiven']
            da2pp_due = request.POST['da2ppDue']
        dv = Da2ppVaccine.objects.create(vaccine_name="da2pp", vaccine_given=da2pp_given, vaccine_due=da2pp_due, dog_id=d.id)

        lepto = request.POST['leptoVac']
        if lepto == "False":
            lepto_given = "1999-01-01"
            lepto_due = today
        
        elif lepto == "True":
            lepto_given = request.POST['leptoGiven']
            lepto_due = request.POST['leptoDue']
        lv = Vaccine.objects.create(vaccine_name="lepto", vaccine_given=lepto_given, vaccine_due=lepto_due, dog_id=d.id)

        bord = request.POST['bordVac']
        if bord == "False":
            bord_given = "1999-01-01"
            bord_due = today

        elif bord == "True":    
            bord_given = request.POST['bordGiven']
            bord_due = request.POST['bordDue']
        bv = Vaccine.objects.create(vaccine_name="bord", vaccine_given=bord_given, vaccine_due=bord_due, dog_id=d.id)

        civ = request.POST['civVac']
        if civ == "False":
            civ_given = "1999-01-01"
            civ_due = today

        elif civ == "True":
            civ_given = request.POST['civGiven']
            civ_due = request.POST['civDue']    
        cv = Vaccine.objects.create(vaccine_name="civ", vaccine_given=civ_given, vaccine_due=civ_due, dog_id=d.id)

        # ************************    PREVENTIONS

        heartworm_prev_due = request.POST['heartwormPrevDue']
        hwp = Prevention.objects.create(prevention_name="heartworm", prevention_due=heartworm_prev_due, dog_id=d.id)

        flea_tick_due = request.POST['fleaPrevDue']
        ftp = Prevention.objects.create(prevention_name="fleaTick", prevention_due=flea_tick_due, dog_id=d.id)

        heartworm_test_due = request.POST['heartwormTestDue']
        hwt = Test.objects.create(test_name="heartworm", test_due=heartworm_test_due, dog_id=d.id)

        fecal_test_due = request.POST['fecalTestDue']
        fft = Test.objects.create(test_name="fecal", test_due=fecal_test_due, dog_id=d.id)

        dewormer_due = request.POST['dewormerTestDue']
        dwt = Test.objects.create(test_name="dewormer", test_due=dewormer_due, dog_id=d.id)
        

    return redirect ('/our_dogs')


def select(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = RabiesVaccine.objects.filter(dog_id=dog_id)
    current_da2pp = Da2ppVaccine.objects.filter(dog_id=dog_id)
    current_lepto = Vaccine.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = Vaccine.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = Vaccine.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = Prevention.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = Prevention.objects.filter(dog_id=dog_id, prevention_name="fleaTick")
    current_heartworm_test = Test.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = Test.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = Test.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
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

def delete(request, dog_id):
    dog = Dog.objects.filter(id=dog_id)
    dog.delete()
    
    return redirect('/our_dogs')

def select_day(request, dog_id):
    current_dog = Dog.objects.filter(id=dog_id)
    current_rabies = RabiesVaccine.objects.filter(dog_id=dog_id)
    current_da2pp = Da2ppVaccine.objects.filter(dog_id=dog_id)
    current_lepto = Vaccine.objects.filter(dog_id=dog_id, vaccine_name="lepto")
    current_bord = Vaccine.objects.filter(dog_id=dog_id, vaccine_name="bord")
    current_civ = Vaccine.objects.filter(dog_id=dog_id, vaccine_name="civ")
    current_heartworm_prev = Prevention.objects.filter(dog_id=dog_id, prevention_name="heartworm")
    current_flea_tick = Prevention.objects.filter(dog_id=dog_id, prevention_name="fleaTick")
    current_heartworm_test = Test.objects.filter(dog_id=dog_id, test_name="heartworm")
    current_fecal = Test.objects.filter(dog_id=dog_id, test_name="fecal")
    current_dewormer = Test.objects.filter(dog_id=dog_id, test_name="dewormer")  
    
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