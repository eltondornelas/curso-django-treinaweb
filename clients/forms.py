from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.Textarea())
    # pode personalizar o formulário
    # {{ form.as_p }} -> para o caso de estar 'apressado'

    class Meta:
        model = Client
        fields = '__all__'
