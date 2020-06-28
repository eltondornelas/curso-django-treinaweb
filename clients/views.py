from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ClientForm, AddressForm
from .entities.client import Client
from .entities.address import Address
from .services import client_service, address_service


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
        form_client = ClientForm(request.POST)
        form_address = AddressForm(request.POST)
        if form_client.is_valid():
            name = form_client.cleaned_data['name']
            sex = form_client.cleaned_data['sex']
            birthday = form_client.cleaned_data['birthday']
            email = form_client.cleaned_data['email']
            profession = form_client.cleaned_data['profession']

            if form_address.is_valid():
                street = form_address.cleaned_data['street']
                number = form_address.cleaned_data['number']
                complement = form_address.cleaned_data['complement']
                district = form_address.cleaned_data['district']
                city = form_address.cleaned_data['city']
                country = form_address.cleaned_data['country']

                new_address = Address(street=street, number=number,
                                      complement=complement, district=district,
                                      city=city, country=country)
                address_db = address_service.register_address(new_address)

                new_client = Client(name=name, sex=sex, birthday=birthday,
                                    email=email, profession=profession,
                                    address=address_db)
                client_service.register_client(new_client)
                return redirect('list_clients')

    else:
        # sem o else ele cria um novo form e perde os erros guardados da
        # instancia que não foi validada
        form_client = ClientForm()
        form_address = AddressForm()

    return render(request, 'clients/form_client.html',
                  {'form_client': form_client,
                   'form_address': form_address})


def list_client_id(request, id):
    client = client_service.list_client_id(id)
    return render(request, 'clients/list_client.html', {'client': client})


def edit_client(request, id):
    client = client_service.list_client_id(id)

    if client.address is None:
        form_address = AddressForm(request.POST or None)
    else:
        address = address_service.list_address_id(client.address.id)
        form_address = AddressForm(request.POST or None, instance=address)

    form_client = ClientForm(request.POST or None, instance=client)

    if form_client.is_valid():
        name = form_client.cleaned_data['name']
        sex = form_client.cleaned_data['sex']
        birthday = form_client.cleaned_data['birthday']
        email = form_client.cleaned_data['email']
        profession = form_client.cleaned_data['profession']

        if form_address.is_valid():
            street = form_address.cleaned_data['street']
            number = form_address.cleaned_data['number']
            complement = form_address.cleaned_data['complement']
            district = form_address.cleaned_data['district']
            city = form_address.cleaned_data['city']
            country = form_address.cleaned_data['country']

            new_address = Address(street=street, number=number,
                                  complement=complement, district=district,
                                  city=city, country=country)

            # caso de cliente antigo que não tem endereço no bd
            if client.address is None:
                address_db = address_service.register_address(new_address)
                new_client = Client(name=name, sex=sex, birthday=birthday,
                                    email=email, profession=profession,
                                    address=address_db)
            else:
                # no código do instrutor é address ao invés de client.address
                # mas acaba levando um warning!
                address_service.edit_address(client.address, new_address)
                new_client = Client(name=name, sex=sex, birthday=birthday,
                                    email=email, profession=profession,
                                    address=client.address)

            client_service.edit_client(client, new_client)
            return redirect('list_clients')

    return render(request, 'clients/form_client.html',
                  {'form_client': form_client,
                   'form_address': form_address})


def remove_client(request, id):
    client = client_service.list_client_id(id)
    address = address_service.list_address_id(client.address.id)

    if request.method == 'POST':
        client_service.remove_client(client)
        address_service.remove_address(address)

        return redirect('list_clients')

    return render(request, 'clients/delete_confirmation.html',
                  {'client': client})
