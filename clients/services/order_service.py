from ..models import Order


def register_order(order):
    Order.objects.create(client=order.client, order_date=order.order_date,
                         value=order.value, status=order.status,
                         observations=order.observations)


def list_orders():
    return Order.objects.all()
