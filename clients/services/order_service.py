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
    # # client -> o nome da relação; select_related é para 1-N ou 1-1
    # orders = Order.objects.prefetch_related('products').all()

    # for i in orders:  # exemplo de pedido com produto N-N (N+1 problem)
        # # print(i.products.name) # qnd coloca o prefetch da erro
        #  print(i.products.all())

    # for i in orders:  # exemplo de cliente com pedido 1-N (N+1 problem)
    #     print(i.client.name)
        # for igual ao do template para mostrar quantas queries fazemos

    # para evitar o problema do N+1, vamos utilizar o join com select_related
    print(connection.queries)
    print(len(connection.queries))

    return orders


def list_order_id(id):
    order = Order.objects.get(id=id)

    # aqui ñ precisa do prefetch pois como já passamos o id, ele já faz o join
    # aqui não precisa desse cuidado, pois é específico
    # o select e o prefetch é quando vai precisar do "todo"
    for i in order.products.all():
        print(i.name)

    print(connection.queries)
    print(len(connection.queries))

    return order


def edit_order(order, new_order):
    order.client = new_order.client
    order.order_date = new_order.order_date
    order.value = new_order.value
    order.status = new_order.status
    order.observations = new_order.observations
    order.products.set(new_order.products)

    order.save(force_update=True)
