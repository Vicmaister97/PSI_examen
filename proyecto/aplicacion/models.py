# -*- coding: utf-8 -*-
# By: Víctor García Carrera

from django.db import models

# Create your models here.
# pizza(id, nombreP)
# ingrediente(id, nombreI)
# contiene(id, pizza(id)foreignKey, ingrediente(id)foreignKey, porcentaje)

class pizza(models.Model):
	#id automatico de Django
	nombreP = models.CharField(max_length=128)

	# Funcion que guarda los datos de una pizza
	def save(self, *args, **kwargs):
		super(pizza, self).save(*args, **kwargs)

	# Definimos el nombre en plural de la clase
	class Meta:
		verbose_name_plural = 'pizzas'

	def __str__(self):
		return "Pizza " + str(self.id) + " de nombre " + self.nombreP


class ingrediente(models.Model):
	# id automatico
	nombreI = models.CharField(max_length=128)

	# Funcion que guarda los datos de un ingrediente
	def save(self, *args, **kwargs):
		super(ingrediente, self).save(*args, **kwargs)

	# Definimos el nombre en plural de la clase
	class Meta:
		verbose_name_plural = 'ingredientes'

	def __str__(self):
		return "Ingrediente " +str(self.id) + " de nombre " + self.nombreI


class contiene(models.Model):
	# id automatico
	pizza = models.ForeignKey(pizza, on_delete=models.CASCADE)
	ingrediente = models.ForeignKey(ingrediente, on_delete=models.CASCADE)
	porcentaje = models.FloatField(default=0.0)

	# Funcion que guarda los datos de contiene
	def save(self, *args, **kwargs):
		super(contiene, self).save(*args, **kwargs)

	# Definimos el nombre en plural de la clase
	class Meta:
		verbose_name_plural = 'contienen'

	def __str__(self):
		return "Contenido " +str(self.id) + " de la pizza " + self.pizza.nombreP + ": ingrediente " + self.ingrediente.nombreI + " en porcentaje " + str(self.porcentaje)
