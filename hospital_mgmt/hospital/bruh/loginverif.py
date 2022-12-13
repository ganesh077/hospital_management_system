from hospital.models import Users
from django.contrib.auth.hashers import make_password, check_password


def confirmreg(user, email, password):

    usr = Users(email=email, uname=user, password=password)
    if usr.save():
        return True
    else:
        return False


def confirmlog(user, password):
    try:
        p = make_password(password)
        user = Users.objects.get(uname=user)
        checkpassword = check_password(password, user.password)
        print(checkpassword)
        if checkpassword:
            uname, login, role = user.uname, True, user.role
        else:
            uname, login, role = "", False, 9
        
        return uname, login, role

    except Exception as e:
        print(str(e))
        uname, login, role = "", False, 9
        return uname, login, role


def userprofile(user):
    try:
        user = Users.objects.get(uname=user)

        return user

    except:
        return ""
