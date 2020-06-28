from django.shortcuts import render, redirect
from ..entities.order import Order
from ..services import order_service

from ..forms import order_forms


def register_order(request):
    if request.method == 'POST':
        form_order = order_forms.OrderForm(request.POST)
        if form_order.is_valid():
            client = form_order.cleaned_data['client']
            observations = form_order.cleaned_data['observations']
            value = form_order.cleaned_data['value']
            status = form_order.cleaned_data['status']
            order_date = form_order.cleaned_data['order_date']

            new_order = Order(client=client, order_date=order_date,
                              value=value, status=status,
                              observations=observations)
            order_service.register_order(new_order)
            return redirect('list_orders')
    else:
        form_order = order_forms.OrderForm()

    return render(request, 'orders/form_order.html',
                  {'form_order': form_order})


def list_orders(request):
    orders = order_service.list_orders()
    return render(request, 'orders/list_orders.html', {'orders': orders})
