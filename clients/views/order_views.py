from django.shortcuts import render, redirect
from ..entities.order import Order
from ..services import order_service

from ..forms.order_forms import OrderForm


def register_order(request):
    if request.method == 'POST':
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            client = form_order.cleaned_data['client']
            observations = form_order.cleaned_data['observations']
            value = form_order.cleaned_data['value']
            status = form_order.cleaned_data['status']
            order_date = form_order.cleaned_data['order_date']
            products = form_order.cleaned_data['products']

            new_order = Order(client=client, order_date=order_date,
                              value=value, status=status,
                              observations=observations, products=products)
            order_service.register_order(new_order)
            return redirect('list_orders')
    else:
        form_order = OrderForm()

    return render(request, 'orders/form_order.html',
                  {'form_order': form_order})


def list_orders(request):
    orders = order_service.list_orders()
    return render(request, 'orders/list_orders.html', {'orders': orders})


def list_order_id(request, id):
    order = order_service.list_order_id(id)
    return render(request, 'orders/list_order.html', {'order': order})


def edit_order(request, id):
    order = order_service.list_order_id(id)
    form_order = OrderForm(request.POST or None, instance=order)

    if form_order.is_valid():
        client = form_order.cleaned_data['client']
        observations = form_order.cleaned_data['observations']
        value = form_order.cleaned_data['value']
        # TODO: criar um filtro para colocar em R$
        status = form_order.cleaned_data['status']
        order_date = form_order.cleaned_data['order_date']

        new_order = Order(client=client, order_date=order_date,
                          value=value, status=status,
                          observations=observations)
        order_service.edit_order(order, new_order)
        return redirect('list_orders')

    return render(request, 'orders/form_order.html',
                  {'form_order': form_order})

# não tem muito sentido criar remoção de pedido
