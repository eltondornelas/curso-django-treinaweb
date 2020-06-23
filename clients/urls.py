from django.urls import path
from .views import *

urlpatterns = [
    path('list', list_clients, name='list_clients'),
    path('register', register_client, name='register_client'),
]
