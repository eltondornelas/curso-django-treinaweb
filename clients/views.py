from django.shortcuts import render
from .models import Client
from .forms import ClientForm


def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/list_clients.html', {'clients': clients})


def register_client(request):
    form = ClientForm()
    return render(request, 'clients/form_client.html', {'form': form})
