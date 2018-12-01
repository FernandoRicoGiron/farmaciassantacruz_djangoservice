from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Promocion)
admin.site.register(Categoria)
admin.site.register(Sucursal)
admin.site.register(Ciudad)
admin.site.register(Estado)