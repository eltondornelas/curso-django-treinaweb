from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=200, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    complement = models.CharField(max_length=200, null=False, blank=False)
    district = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.street


class Client(models.Model):
    SEX_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outros')
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profession = models.CharField(max_length=50, null=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=False,
                           blank=False)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL,
                                   null=True)

    def __str__(self):
        return self.name
