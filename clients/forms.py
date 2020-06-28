from django import forms
from .models import Client, Address


class ClientForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.Textarea())
    # pode personalizar o formulário
    # {{ form.as_p }} -> para o caso de estar 'apressado'

    class Meta:
        model = Client
        fields = ['name', 'sex', 'birthday', 'email', 'profession']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'complement', 'district', 'city',
                  'country']
