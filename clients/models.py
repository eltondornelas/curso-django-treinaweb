from django.db import models
from django.utils import timezone
from django.db.models.signals import m2m_changed


class Address(models.Model):
    street = models.CharField(max_length=200, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    complement = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.street


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    value = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.name


class Client(models.Model):
    SEX_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outros')
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=30, null=False)
    birthday = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profession = models.CharField(max_length=50, null=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=False,
                           blank=False)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL,
                                   null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pedido realizado'),
        ('F', 'Fazendo'),
        ('E', 'Saiu para entrega'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    value = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              blank=False, null=False)
    observations = models.CharField(max_length=50, null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.client.name


def pre_save_product_receiver(sender, instance, action, **kwargs):
    # django-signals  -> m2m_changed
    if action == 'post_add' or action == 'post_remove' or \
            action == 'post_clear':
        # se adicionou, editou/removeu ou limpou todos produtos daquele pedido
        products = instance.products.all()
        total = 0
        for i in products:
            total += i.value

        instance.value = total
        instance.save()


m2m_changed.connect(pre_save_product_receiver, sender=Order.products.through)


'''
python manage.py migrate clients 0005_order

caso precise desfazer uma migração, basta fazer um rollback digitando o 
comando migrate seguido do nome do app seguido do nome da migração que fica
no histórico no diretório migrations.
uma vez executado esse comando as migrações após esse rollback são desativados
e com isso é possível excluir a classe/tabela e o arquivo de migração 
com segurança do seu projeto

'''

'''
# caso precise mapear um bd legado para um projeto django basta:
em settings.py configurar o banco de dados e então digitar:

python manage.py inspectdb > nome_app/models.py


relações OneToOne acabam sendo convertidos para ForeignKey com o atributo
unique=True
'''

'''
# criando uma migração em branco/vazia
python manage.py makemigrations --empty nome_app
'''

'''
# para apagar dados do bd. isso não mexe na estrutura do banco de dados
python manage.py flush
'''