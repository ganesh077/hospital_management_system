from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient, Appointment, Appointments
from .bruh.loginverif import confirmreg, confirmlog
from .bruh.appointmentc import add_appointment, fetch_appointment

# Create your views here.


def About(request):
    if 'login' in request.COOKIES:
        context = {
            "login": True,
            "role": request.COOKIES['user_role']
        }
        response = render(request, 'about.html', context)
        return response
    else:
        context = {
            "login": False
        }
        response = render(request, 'about.html', context)
        return response


def Home(request):
    if 'login' in request.COOKIES:
        context = {
            "login": True,
            "role": request.COOKIES['user_role']
        }
        response = render(request, 'home.html', context)
        print(response)
        return response
    else:
        context = {
            "login": False
        }
        response = render(request, 'home.html', context)
        return response


def Contact(request):
    if 'login' in request.COOKIES:
        context = {
            "login": True,
            "role": request.COOKIES['user_role']
        }
        response = render(request, 'contact.html', context)
        return response
    else:
        context = {
            "login": False
        }
        response = render(request, 'contact.html', context)
        return response


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d = 0
    p = 0
    a = 0
    for i in doctors:
        d += 1
    for i in patient:
        p += 1
    for i in appointment:
        a += 1
    d1 = {'d': d, 'p': p, 'a': a}
    return render(request, 'index.html', d1)


def Login(request):
    context = {
        "login": False
    }
    if 'login' in request.COOKIES:
        context = {
            "login": True,
            "role": request.COOKIES['user_role']
        }
        response = HttpResponseRedirect('/', context)
        return response

    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        uname, login, role = confirmlog(u, p)
        if login == True:
            context = {
                "login": True,
            }
            response = HttpResponseRedirect('/', context)
            response.set_cookie('username', uname)
            response.set_cookie('login', login)
            response.set_cookie('user_role', role)
            return response
        else:
            response = render(request, 'login.html', context)
            return response

    response = render(request, 'login.html', context)

    return response


def Logout_admin(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    response.delete_cookie('login')
    response.delete_cookie('user_role')
    return response


def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def register(request):
    error = ""
    if request.method == "POST":
        email = request.POST['email']
        uname = request.POST['username']
        password = request.POST['password']
        flag = confirmreg(uname, email, password)
        if flag == True:
            error = "yes"
        else:
            error = "no"

    d = {"error": error}
    return render(request, 'register.html', d)


def Delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def Add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']

        try:
            Doctor.objects.create(Name=n, mobile=m, special=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}

    return render(request, 'add_doctor.html', d)


def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc': doc}
    return render(request, 'view_patient.html', d)


def Delete_patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def Add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']

        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def Add_appointment(request):
    context = {
        "login": False
    }
    if 'login' in request.COOKIES:
        context = {
            "login": True,
            "role": request.COOKIES['user_role'],
            "user": request.COOKIES['username']
        }

        if request.method == "POST":
            u = request.COOKIES['username']
            d = request.POST['date']
            doc = request.POST['doctor']
            t = request.POST['time']
            state = add_appointment(u, d, t, doc)
            if state == True:
                context = {
                    "code": 1,
                }
                response = HttpResponseRedirect('view_appointment/', context)
                return response

        response = render(request, 'add_appointment.html', context)
        return response
    response = render(request, 'add_appointment.html', context)

    return response


def View_appointment(request):
    context = {
        "login": False
    }
    if 'login' in request.COOKIES:
        context = {
            "login": True,
            "role": request.COOKIES['user_role'],
            "user": request.COOKIES['username']
        }

        if request.method == "GET":
            u = request.COOKIES['username']
            r = request.COOKIES['user_role']
            state = fetch_appointment(u, r)
            context = {
                "login": True,
                "role": request.COOKIES['user_role'],
                "user": request.COOKIES['username'],
                "data": state
            }
            response = render(request, 'view_appointment.html', context)
            return response

        response = render(request, 'view_appointment.html', context)
        return response
    response = render(request, 'view_appointment.html', context)

    return response


def Delete_appointment(request, pid):
    if 'login' in request.COOKIES:
        context = {
            "login": True,
            "role": request.COOKIES['user_role'],
            "user": request.COOKIES['username']
        }
        app = Appointments.objects.get(id=pid)
        app.delete()
        return redirect('view_appointment')


def User_profile(request):
    context = {
        "login": False
    }
    if 'login' in request.COOKIES:
        context = {
            "login": True,
            "role": request.COOKIES['user_role'],
            "user": request.COOKIES['username']
        }

        if request.method == "GET":
            u = request.COOKIES['username']
            r = request.COOKIES['user_role']
            context = {
                "login": True,
                "role": request.COOKIES['user_role'],
                "user": request.COOKIES['username'],
            }
            response = render(request, 'profile.html', context)
            return response

        response = render(request, 'profile.html', context)
        return response
    response = render(request, '/', context)

    return response
