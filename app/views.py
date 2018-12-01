from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def categorias(request):
	categorias = Categoria.objects.all()
	data = {}
	for categoria in categorias:
		i = 1
		data[i] = {
			"id":categoria.id,
			"categoria":categoria.Categoria
		}
		i += 1
	return JsonResponse(data, safe=False)

def productos(request):
	productos = Producto.objects.all()
	data = {}
	for producto in productos:
		i = 1
		data[i] = {
			"id":producto.id,
			"nombre":producto.Nombre,
			"precio":producto.Precio,
			"descripcion":producto.Descripcion,
			"categoria":producto.Categoria.Categoria,
			"imagen":producto.Imagen.url}
		i += 1
	return JsonResponse(data, safe=False)

def productosc(request):
	categoria = Categoria.objects.get(id = request.GET.get("categoria"))
	productos = Producto.objects.filter(Categoria = categoria)
	data = {}
	for producto in productos:
		i = 1
		data[i] = {
			"nombre":producto.Nombre,
			"precio":producto.Precio,
			"descripcion":producto.Descripcion,
			"categoria":producto.Categoria.Categoria,
			"imagen":producto.Imagen.url
		}
		i += 1
	return JsonResponse(data, safe=False)

def promociones(request):
	promociones = Promocion.objects.all()
	data = {}
	for promocion in promociones:
		i = 1
		data[i] = {
			"id":promocion.id,
			"nombre":promocion.Nombre,
			"precio":promocion.Precio,
			"descripcion":promocion.Descripcion,
			"categoria":promocion.Categoria.Categoria,
			"imagen":promocion.Imagen.url
		}
		i += 1
	return JsonResponse(data, safe=False)

	
def estados(request):
	estados = Estado.objects.all()
	data = {}
	for estado in estados:
		i = 1
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
	for ciudad in ciudades:
		i = 1
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
	for sucursal in sucursales:
		i = 1
		data[sucursal.id] = {
			"id":sucursal.id,
			"nombre":sucursal.Nombre,
			"direccion":sucursal.Direccion,
			"imagen":sucursal.Imagen.url,
			"horario":sucursal.Horario,
			"telefono":sucursal.Telefono
			}
		i += 1
	return JsonResponse(data, safe=False)