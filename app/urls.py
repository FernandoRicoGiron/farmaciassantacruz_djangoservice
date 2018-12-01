from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path

urlpatterns = [
	# re_path('cliente/(?P<empresa>[\w|\W]+)', views.previa),
    re_path('productos/', views.productos),
    re_path('productosc/', views.productosc),
    path('promociones/', views.promociones),
    path('estados/', views.estados),
    re_path('ciudades/', views.ciudades),
    re_path('sucursales/', views.sucursales),
    re_path('categorias/',views.categorias)
]