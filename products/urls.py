from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/<int:my_id>/', views.dynamic_lookup_view, name='dynamic_lookup_view'),
    path('products/', views.product_detail_view, name='product_detail_view'),
    path('create/', views.product_create_view, name='product_create_view'),
    path('', views.home_view, name='home'),
]
