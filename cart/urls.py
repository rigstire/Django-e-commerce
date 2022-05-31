from django.urls import path 
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('<int:id>/', views.cart_add, name='cart_add'),
    path('remove/<int:id>/', views.cart_remove, name='cart_remove'),
]