from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def productos(request):
	productos = Producto.objects.all()
	data = {}
	for producto in productos:
		data[producto.id] = {"nombre":producto.Nombre,
			"precio":producto.Precio,
			"descripcion":producto.Descripcion,
			"categoria":producto.Categoria.Categoria,
			"imagen":producto.Imagen.url}
	return JsonResponse(data, safe=False)

def promociones(request):
	promociones = Promocione.objects.all()
	data = {}
	for promocion in promociones:
		data[promocion.id] = {"nombre":promocion.Nombre,
			"precio":promocion.Precio,
			"descripcion":promocion.Descripcion,
			"categoria":promocion.Categoria.Categoria,
			"imagen":promocion.Imagen.url}
	return JsonResponse(data, safe=False)

	
