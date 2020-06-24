from django.urls import path
from .views import *

urlpatterns = [
    path('list', list_clients, name='list_clients'),
    path('register', register_client, name='register_client'),
    path('list/<int:id>', list_client_id, name='list_client_id'),
    path('edit/<int:id>', edit_client, name='edit_client'),
    path('remove/<int:id>', remove_client, name='remove_client'),
]
