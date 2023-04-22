"""Banco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from proyectos.views.buscar_proyecto import ProyectoList
from proyectos.views.registrar import register
from proyectos.views.iniciar_sesion import UserLoginAPIView
from proyectos.views.cerrar_sesion import logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('proyectos.urls')),
    #path('create_user/', registrar.register_users_from_excel(), name='create_user'),
    # path('api/', include('djoser.urls')),
    # path('api/', include('djoser.urls.authtoken')),
    path('register/', register),
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', logout_view),
    path('buscar_proyectos/', ProyectoList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('allauth.urls')),
   

]
