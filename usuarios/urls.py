from django.urls import path
from . import views



urlpatterns=[
    path('', views.index, name="index"),
    path('prods', views.prods, name="productos"),
    path('carrito', views.carrito, name="carrito"),
    path('quienSomos', views.quienSomos, name="quienSomos"),
    path('registro', views.registro, name="registro"),
    path('agregar/<str:pk>/', views.agregar_producto, name="Add"),
    path('eliminar/<str:pk>/', views.eliminar_producto, name="Del"),
    path('restar/<str:pk>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('marcas', views.marcas, name="marcas")
]