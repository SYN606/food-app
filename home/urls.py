from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='/'),
    path('login', views.login, name='login'),
    path('create_acc', views.create_account, name='create_acc')
]
