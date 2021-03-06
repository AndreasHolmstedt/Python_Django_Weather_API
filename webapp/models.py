# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=26)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"
