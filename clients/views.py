from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ClientForm
from .entities.client import Client
from .services import client_service


def list_clients(request):
    clients = client_service.list_clients()
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
            name = form.cleaned_data['name']
            sex = form.cleaned_data['sex']
            birthday = form.cleaned_data['birthday']
            email = form.cleaned_data['email']
            profession = form.cleaned_data['profession']

            new_client = Client(name=name, sex=sex, birthday=birthday,
                                       email=email, profession=profession)
            client_service.register_client(new_client)
            return redirect('list_clients')

    else:
        # sem o else ele cria um novo form e perde os erros guardados da
        # instancia que não foi validada
        form = ClientForm()

    return render(request, 'clients/form_client.html', {'form': form})


def list_client_id(request, id):
    client = client_service.list_client_id(id)
    return render(request, 'clients/list_client.html', {'client': client})


def edit_client(request, id):
    client = client_service.list_client_id(id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        name = form.cleaned_data['name']
        sex = form.cleaned_data['sex']
        birthday = form.cleaned_data['birthday']
        email = form.cleaned_data['email']
        profession = form.cleaned_data['profession']

        new_client = Client(name=name, sex=sex, birthday=birthday,
                                   email=email, profession=profession)
        client_service.edit_client(client, new_client)
        return redirect('list_clients')

    return render(request, 'clients/form_client.html', {'form': form})


def remove_client(request, id):
    client = client_service.list_client_id(id)

    if request.method == 'POST':
        client_service.remove_client(client)
        return redirect('list_clients')

    return render(request, 'clients/delete_confirmation.html',
                  {'client': client})
