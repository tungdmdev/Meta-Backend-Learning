"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('say_hello/', views.say_hello),
    path('homepage/', views.homepage),
    path('display_date/', views.display_date),
    path('menu/', views.menu),
    path('main/', include('myapp.urls')),
    path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"), 
    path("getform/", views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems), #dish=pasta

    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), #Mapping URLs with Params
]
