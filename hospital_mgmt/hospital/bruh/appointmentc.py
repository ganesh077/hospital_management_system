from hospital.models import Appointments

def add_appointment(user, date, time, doctor):
    apt = Appointments(doctor=doctor, patient=user, date=date, time=time)
    if apt.save():
        return True
    else:
        return False

def fetch_appointment(username = None, role = None):
    apt = Appointments.objects.filter(patient=username)
    if apt != "":
        return apt
    else:
        return False

def fetchallappointment(username = None, role = None):
    apt = Appointments.objects.all()
    if apt != "":
        return apt
    else:
        return False