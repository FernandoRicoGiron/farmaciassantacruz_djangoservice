from __future__ import unicode_literals
import os, sys
from django.db import models
from django.utils import timezone
import datetime
from django.db import migrations
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
import json

# Create your models here.
class Categoria(models.Model):
	Categoria = models.CharField(max_length=100)

	def __str__(self):
		return self.Categoria

class Producto(models.Model):
	Nombre = models.CharField(max_length=100)
	Precio = models.IntegerField(default=0)
	Descripcion = models.TextField()
	Imagen = models.ImageField(upload_to="Previo")
	Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

	def __str__(self):
		return self.Nombre

class Promocione(models.Model):
	Nombre = models.CharField(max_length=100)
	Precio = models.IntegerField(default=0)
	Descripcion = models.TextField()
	Imagen = models.ImageField(upload_to="Previo")
	Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

	def __str__(self):
		return self.Nombre