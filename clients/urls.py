from django.urls import path
from clients.views.client_views import *
from clients.views.order_views import *
from clients.views.product_views import *

urlpatterns = [
    path('list_clients', list_clients, name='list_clients'),
    path('register_client', register_client, name='register_client'),
    path('list_client/<int:id>', list_client_id, name='list_client_id'),
    path('edit_client/<int:id>', edit_client, name='edit_client'),
    path('remove_client/<int:id>', remove_client, name='remove_client'),

    path('register_order', register_order, name='register_order'),
    path('list_orders', list_orders, name='list_orders'),
    path('list_order/<int:id>', list_order_id, name='list_order_id'),
    path('edit_order/<int:id>', edit_order, name='edit_order'),

    path('register_product', register_product, name='register_product'),
    path('list_products', list_products, name='list_products'),
    path('list_product/<int:id>', list_product_id, name='list_product_id'),
    path('edit_product/<int:id>', edit_product, name='edit_product'),
]
