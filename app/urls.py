from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path

urlpatterns = [
	# re_path('cliente/(?P<empresa>[\w|\W]+)', views.previa),
	path('productos/', views.productos),
    path('promociones/', views.promociones),

]