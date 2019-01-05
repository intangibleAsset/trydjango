from django.http import HttpResponse
from django.shortcuts import render
from . models import Product
from . forms import ProductForm
# Create your views here.
def home_view(request):
    return render(request, "products/start_page.html",{"title":"home page"})

def product_detail_view(request):
    obj = Product.objects.get(id=5)
#    context = {
#    'title': obj.title,
#    'description': obj.description
#    }
    context = {"object":obj}
    return render(request,"products/detail.html",context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form":form
    }
    return render(request,"products/product_create.html",context)
