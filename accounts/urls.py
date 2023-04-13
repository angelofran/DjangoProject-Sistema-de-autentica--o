from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logIn, name='logIn'),
    path('logout/', views.logOut, name='logOut'),
    path('signup/', views.signUp, name='signUp'),
    path('home/', views.home, name='home'),
]
