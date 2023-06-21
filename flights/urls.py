from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path("<int:single_flight_id>",views.single_flight, name='single_flight'),
    path("<int:single_flight_id>/book",views.book, name='book'),

] 
