from django.urls import path
from clients.views.client_views import *
from clients.views.order_views import *

urlpatterns = [
    path('list_clients', list_clients, name='list_clients'),
    path('register_client', register_client, name='register_client'),
    path('list_client/<int:id>', list_client_id, name='list_client_id'),
    path('edit_client/<int:id>', edit_client, name='edit_client'),
    path('remove_client/<int:id>', remove_client, name='remove_client'),
    path('register_order', register_order, name='register_order'),
    path('list_orders', list_orders, name='list_orders'),
]
