"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views
from django.conf import settings
from django.conf.urls.static import static

#including urls for generating REST API link corresponding to each table in the database of the app

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^House/', views.HouseList.as_view()),
    url(r'^mem_details/', views.mem_detailsList.as_view()),
    url(r'^imagetable/', views.imagetableList.as_view()),
 	url(r'^videotable/', views.videotableList.as_view()),
 	url(r'^FarmTable/', views.FarmTableList.as_view()),
 	url(r'^farmpoints/', views.farmpointsList.as_view()),
 	url(r'^farmcroptable/', views.farmcroptableList.as_view()),
 	url(r'^welltable/', views.welltableList.as_view()),
	url(r'^wellinfo/', views.wellinfoList.as_view()),   
    url(r'^newfarmcroptable/', views.newfarmcroptableList.as_view()),	   		
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





urlpatterns=format_suffix_patterns(urlpatterns)
