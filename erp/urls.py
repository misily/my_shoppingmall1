from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('erp/', views.erp, name='erp'),
    path('erp/productlist/', views.product_list, name='product-list'),
    path('erp/inbound', views.product_inbound, name='product-inbound'),
    path('erp/outbound', views.product_outbound, name= 'product-outbound'),
]
