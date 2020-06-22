from django.db import models


class Client(models.Model):
    SEX_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('N', 'Nenhuma das opções')
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profession = models.CharField(max_length=50, null=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=False,
                           blank=False)

    def __str__(self):
        return self.name
