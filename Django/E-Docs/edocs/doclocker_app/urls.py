from django.urls import path
from . import views




urlpatterns = [
    path('home/', views.DLock, name='DLock'),
    #path('homepage/', views.homepage, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.aboutus, name='aboutus'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout/', views.login, name='logout'),
]