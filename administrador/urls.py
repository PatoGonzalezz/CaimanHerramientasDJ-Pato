from django.urls import path
from . import views

urlpatterns=[
    path('listaProds', views.lista_productos, name='lista_productos'),
    path('addProd', views.agregar_productos, name='addProd'),
    path('deletProd/<str:pk>', views.eliminar_productos, name='delete_producto'),
    path('findProd/<str:pk>', views.buscar_productos, name='editar_ProductFind'),
    path('editProd', views.actualizar_productos, name="actualizar_productos"),
    path('', views.menu, name='menu'),
    path('register/', views.register, name="register" ),
    
    
    path('listar_tipos',views.lista_tipos,name='crud_tipos'),
    path('agregar_tipo',views.agregar_tipo,name='tiposAdd'),
    path('borrar_tipo/<int:pk>',views.borrar_tipo,name='tiposDel'),
    path('buscar_tipo/<int:pk>', views.buscar_tipo, name='tiposFind'),
    path('actualizar_tipo',views.actualizar_tipo,name='tiposEdit'),
]