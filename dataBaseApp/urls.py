from django.contrib.auth.views import LogoutView
from django.urls import path

from dataBaseApp.views import *
from dataBaseApp.controller import search_rocks, search_rock

urlpatterns = [
    path('', login_view, name='login'),
    path('register', register_view, name='register_view'),
    path('page', page_view, name='page'),
    path('search/', search_rocks, name='search_rocks'),
    path('searchs/', search_rock, name='search_rock'),
    path('add/', addRock, name='addRock'),

    path('delete/', delete_record, name='delete'),


    path('loginn/', loginn, name='login'),
    path('registerr/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('schema/', schema, name='schema')
]
