from django.urls import path
from hospital.views import About,Home,Contact,Login,Logout_admin,Index,View_doctor,Delete_doctor,Add_doctor,View_patient,Delete_patient,Add_patient,User_profile,View_appointment,Add_appointment,register,Delete_appointment

urlpatterns = [
     path('', Home, name='home'),
     path('about/', About, name='about'),
     path('contact/', Contact, name='contact'),
     path('alogin/', Login, name='login_admin'),
      path('login/', Login, name='login'),
     path('logout/', Logout_admin, name='logout_admin'),
     path('index/', Index, name='dashboard'),
     path('view_doctor/', View_doctor, name='view_doctor'),
     path('view_patient/', View_patient, name='view_patient'),
     path('view_appointment/', View_appointment, name='view_appointment'),
     path('add_doctor/', Add_doctor, name='add_doctor'),
     path('register', register, name='register'),
     path('add_patient/', Add_patient, name='add_patient'),
     path('add_appointment/', Add_appointment, name='add_appointment'),
     path('delete_doctor(?P<int:pid>)/', Delete_doctor, name='delete_doctor'),
     path('delete_patient(?P<int:pid>)/', Delete_patient, name='delete_patient'),
     path('delete_appointment(?P<int:pid>)/', Delete_appointment, name='delete_appointment'),
     path('profile/', User_profile, name='view_profile'),
]