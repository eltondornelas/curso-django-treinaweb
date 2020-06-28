from django import forms
from clients.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'complement', 'district', 'city',
                  'country']
