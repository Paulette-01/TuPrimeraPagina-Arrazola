
from django.urls import path
from . import views

urlpatterns = [
    path('patient/list', views.patient_list, name='patient_list'),
    path('patient/create', views.patient_create, name='patient_create')
]
