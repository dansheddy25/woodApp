from django.conf.urls import include
from django.urls import re_path
from django.urls import path 

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('users/delete', views.user_delete_view, name='user_delete_view'),
    path('users/', views.user_view, name='user_view'),
]