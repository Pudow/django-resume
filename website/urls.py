from django.urls import path, include
from . import views

#The ''  is for the section of the page. 
#In this case its the main page. 
urlpatterns = [
    path('', views.home, name= 'home'),
    path('about',views.about, name = 'about',)
]
