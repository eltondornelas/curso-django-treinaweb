from ..models import Client


def list_clients():
    clients = Client.objects.all()
    # clients = Client.objects.using('read').all()
    # para informar qual conexão de leitura. esse é o formato manual sem router
    # clients = Client.objects.filter(sex='F').all()
    '''
    # clients = Client.objects.filter(sex='F', birthday > '1990-01-01').all()
    # clients = Client.objects.exclude(sexo='F', birthday > '1990-01-01')
    os dois exemplos acima estavam no material do curso, porém acredito estar
    equivocado, o correto seria:
     (birthday__gt='1990-01-01')
    '''

    return clients


def list_client_id(id):
    client = Client.objects.get(id=id)
    return client


def register_client(client):
    Client.objects.create(name=client.name, lastname=client.lastname,
                          sex=client.sex, birthday=client.birthday,
                          email=client.email, profession=client.profession,
                          address=client.address)


def edit_client(client, new_client):
    client.name = new_client.name
    client.lastname = new_client.lastname
    client.sex = new_client.sex
    client.birthday = new_client.birthday
    client.email = new_client.email
    client.profession = new_client.profession
    client.address = new_client.address

    client.save(force_update=True)


def remove_client(client):
    client.delete()
