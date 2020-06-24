from ..models import Client


def list_clients():
    clients = Client.objects.all()
    return clients


def list_client_id(id):
    client = Client.objects.get(id=id)
    return client


def register_client(client):
    Client.objects.create(name=client.name, sex=client.sex,
                          birthday=client.birthday, email=client.email,
                          profession=client.profession)


def edit_client(client, new_client):
    client.name = new_client.name
    client.sex = new_client.sex
    client.birthday = new_client.birthday
    client.email = new_client.email
    client.profession = new_client.profession

    client.save(force_update=True)


def remove_client(client):
    client.delete()