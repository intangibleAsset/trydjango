from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_detail_view, name='product_detail_view'),
    path('', views.home_view, name='home'),
]
