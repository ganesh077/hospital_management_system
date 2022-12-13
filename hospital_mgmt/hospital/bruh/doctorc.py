from hospital.models import Doctor


def fetchdoctors(r=0):

    doc = Doctor.objects.all()
    print(doc)
    return doc


def adddoctor(r=0, name=None, mobile=None, special=None):
    doc = Doctor(Name=name, mobile=mobile, special=special)
    if doc.save():
        return True
    else:
        return False