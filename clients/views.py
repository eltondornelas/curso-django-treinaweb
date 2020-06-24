from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm


def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/list_clients.html', {'clients': clients})


def register_client(request):
    """
    # ñ precisa do action do form que ele esta renderizado por este método
        logo ele sabe que o submit é um request para este método
    # csrf_token é um hash que garante que este form está sendo recebido por
        uma aplicação que ele conhece do django
    """

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clients')

    else:
        # sem o else ele cria um novo form e perde os erros guardados da
        # instancia que não foi validada
        form = ClientForm()

    return render(request, 'clients/form_client.html', {'form': form})


def list_client_id(request, id):
    client = Client.objects.get(id=id)
    return render(request, 'clients/list_client.html', {'client': client})


def edit_client(request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('list_clients')

    return render(request, 'clients/form_client.html', {'form': form})


def remove_client(request, id):
    client = Client.objects.get(id=id)

    if request.method == 'POST':
        client.delete()
        return redirect('list_clients')

    return render(request, 'clients/delete_confirmation.html',
                  {'client': client})
