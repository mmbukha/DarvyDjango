
from django.contrib import admin
from django.urls import path
from poolapp import  views

urlpatterns = [
    path('', admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('form/', views.form,name='form'),

]
