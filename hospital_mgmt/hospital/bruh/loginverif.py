from hospital.models import Users


def confirmreg(user, email, password):

    usr = Users(email=email, uname=user, password=password)
    if usr.save():
        return True
    else:
        return False


def confirmlog(user, password):

    try:
        user = Users.objects.get(uname=user, password=password)
        uname, login, role = user.uname, True, user.role
        return uname, login, role

    except:
        uname, login, role = "", False, 9
        return uname, login, role