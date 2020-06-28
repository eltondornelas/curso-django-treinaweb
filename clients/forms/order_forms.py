from django import forms
from ..models import Order, Client


class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    # instrutor colocou a linha acima, porém acredito que isso já é o que
    # acontece por padrão.

    class Meta:
        model = Order
        fields = ['client', 'observations', 'order_date', 'value', 'status']
