from __future__ import unicode_literals

from django.db import models

# Criar os models aqui.
class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        rg = models.CharField(max_length=8)

        def __unicode__(self):
                return self.nome
