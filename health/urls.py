
from django.urls import path
from . import views

urlpatterns = [
    path('',views.appointment, name='home'),
    path('contact/',views.contact,name='contact'),
]
