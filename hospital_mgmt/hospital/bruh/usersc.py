from hospital.models import Users

def listusers(r=None):
    try:
        user = Users.objects.filter(role=0)
        return user

    except:
        return ""