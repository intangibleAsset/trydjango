from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/product_list_view', views.product_list_view, name='product_list_view'),
    path('products/<int:id>/delete/',views.product_delete_view, name='product_delete'),
    path('products/<int:my_id>/', views.dynamic_lookup_view, name='dynamic_lookup_view'),
    path('products/', views.product_detail_view, name='product_detail_view'),
    path('create/', views.product_create_view, name='product_create_view'),
    path('', views.home_view, name='home'),
]
