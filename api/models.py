from pickle import TRUE
from django.db import models


class Meucep(models.Model):
    cep = models.CharField(max_length=8, unique=True)
    cidade = models.CharField(max_length=512)
    bairro = models.CharField(max_length=512, null=True)
    rua = models.CharField(max_length=512, null=True)
    # complemento = models.CharField(max_length=200)

    def __str__(self):
        return self.cep
