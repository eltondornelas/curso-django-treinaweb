from ..models import Order
from .product_service import *
from django.db import connection


def register_order(order):
    order_db = Order.objects.create(client=order.client,
                                    order_date=order.order_date,
                                    value=order.value, status=order.status,
                                    observations=order.observations)
    order_db.save()
    # não ficou claro o porque do save logo após o create
    for i in order.products:
        product = list_product_id(i.id)
        order_db.products.add(product)


def list_orders():
    # orders = Order.objects.all()
    orders = Order.objects.select_related('client').all()
    # client -> o nome da relação

    for i in orders:
        print(i.client.name)
        # for igual ao do template para mostrar quantas queries fazemos

    # para evitar o problema do N+1, vamos utilizar o join com select_related
    print(connection.queries)
    print(len(connection.queries))

    return orders


def list_order_id(id):
    order = Order.objects.get(id=id)
    return order


def edit_order(order, new_order):
    order.client = new_order.client
    order.order_date = new_order.order_date
    order.value = new_order.value
    order.status = new_order.status
    order.observations = new_order.observations
    order.products.set(new_order.products)

    order.save(force_update=True)
