from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name="home"),
    path("about",views.about,name= 'about'),
    path("contact",views.contact,name= 'contact'),
    path("login",views.loginuser,name= 'login'),
    path("signup",views.signup,name= 'signup'),
    path("main",views.main,name= 'main'),
    path("logout",views.logoutuser,name= 'logout'),
    path("course",views.course,name= 'course'),
    path("python",views.python,name= 'python'),
    path("cpp",views.cpp,name= 'cpp'),
    path("c",views.c,name= 'c'),
    path("dart",views.dart,name= 'dart'),
    path("js",views.js,name= 'js'),
    path("java",views.java,name= 'java'),
    
    
]
