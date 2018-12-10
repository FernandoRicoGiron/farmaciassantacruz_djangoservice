from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def categorias(request):
	categorias = Categoria.objects.all()
	data = {}

	i = 1
	for categoria in categorias:
		data[i] = {
			"id":categoria.id,
			"categoria":categoria.Categoria
		}
		i += 1
	return JsonResponse(data, safe=False)

def productos(request):
	productos = Producto.objects.all()
	data = {}

	i = 1
	for producto in productos:
		data[i] = {
			"id":producto.id,
			"nombre":producto.Nombre,
			"precio":producto.Precio,
			"descripcion":producto.Descripcion,
			"categoria":producto.Categoria.Categoria,
			"imagen":producto.Imagen}
		i += 1
	return JsonResponse(data, safe=False)

def productosc(request):
	categoria = Categoria.objects.get(id = request.GET.get("categoria"))
	productos = Producto.objects.filter(Categoria = categoria)
	data = {}

	i = 1
	for producto in productos:
		data[i] = {
			"nombre":producto.Nombre,
			"precio":producto.Precio,
			"descripcion":producto.Descripcion,
			"categoria":producto.Categoria.Categoria,
			"imagen":producto.Imagen
		}
		i += 1
	return JsonResponse(data, safe=False)

def promociones(request):
	promociones = Promocion.objects.all()
	data = {}

	i = 1
	for promocion in promociones:
		data[i] = {
			"id":promocion.id,
			"nombre":promocion.Nombre,
			"precio":promocion.Precio,
			"descripcion":promocion.Descripcion,
			"categoria":promocion.Categoria.Categoria,
			"imagen":promocion.Imagen
		}
		i += 1

	return JsonResponse(data, safe=False)

	
def estados(request):
	estados = Estado.objects.all()
	data = {}
	i = 1
	for estado in estados:
		data[i] = {
			"id":estado.id,
			"nombre":estado.Nombre,
		}
		i += 1
	return JsonResponse(data, safe=False)

def ciudades(request):
	estado = Estado.objects.get(id = request.GET.get("estado"))
	ciudades = Ciudad.objects.filter(Estado=estado)
	data = {}

	i = 1
	for ciudad in ciudades:
		data[i] = {
			"id":ciudad.id,
			"nombre":ciudad.Nombre
		}
		i += 1
	return JsonResponse(data, safe=False)

def sucursales(request):
	ciudad = Ciudad.objects.get(id=request.GET.get("ciudad"))
	sucursales = Sucursal.objects.filter(Ciudad = ciudad)
	data = {}

	i = 1
	for sucursal in sucursales:
		data[sucursal.id] = {
			"id":sucursal.id,
			"nombre":sucursal.Nombre,
			"direccion":sucursal.Direccion,
			"imagen":sucursal.Imagen,
			"horario":sucursal.Horario,
			"telefono":sucursal.Telefono
			}
		i += 1
	return JsonResponse(data, safe=False)