from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('clothing/',views.clothing, name='clothing'),
    path('shoes/',views.shoes, name='shoes'),
    path('accessories/', views.accessories, name='accessories'),
    path('add/<int:id>',views.add_item, name='add_item'),
    path('cart/',views.cart_detail, name='cart_detail'),
    path('cart/<int:id>', views.delete_item, name='delete_item'),
]