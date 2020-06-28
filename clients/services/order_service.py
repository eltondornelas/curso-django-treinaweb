from ..models import Order


def register_order(order):
    Order.objects.create(client=order.client, order_date=order.order_date,
                         value=order.value, status=order.status,
                         observations=order.observations)


def list_orders():
    return Order.objects.all()


def list_order_id(id):
    order = Order.objects.get(id=id)
    return order


def edit_order(order, new_order):
    order.client = new_order.client
    order.order_date = new_order.order_date
    order.value = new_order.value
    order.status = new_order.status
    order.observations = new_order.observations

    order.save(force_update=True)
