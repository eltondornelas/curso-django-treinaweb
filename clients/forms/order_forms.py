from django import forms
from ..models import Order, Client


class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all())

    class Meta:
        model = Order
        fields = ['client', 'observations', 'order_date', 'value', 'status']
