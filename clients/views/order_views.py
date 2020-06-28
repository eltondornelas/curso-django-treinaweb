from django.shortcuts import render

from ..forms import order_forms


def register_order(request):
    form_order = order_forms.OrderForm()
    return render(request, 'orders/form_order.html',
                  {'form_order': form_order})
