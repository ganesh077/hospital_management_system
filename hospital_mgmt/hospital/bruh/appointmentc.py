from hospital.models import Appointments

def add_appointment(user, date, time, doctor):
    apt = Appointments(doctor=doctor, patient=user, date=date, time=time)
    if apt.save():
        return True
    else:
        return False

def fetch_appointment(username = None, role = None):
    apt = Appointments.objects.filter(patient=username)
    print(apt[0].patient)
    if apt != "":
        return apt
    else:
        return False