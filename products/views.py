from django.http import HttpResponse
from django.shortcuts import render
from . models import Product
# Create your views here.
def home_view(request):
    return render(request, "products/start_page.html",{"title":"home page"})

def product_detail_view(request):
    obj = Product.objects.get(id=1)
#    context = {
#    'title': obj.title,
#    'description': obj.description
#    }
    context = {"object":obj}
    return render(request,"products/detail.html",context)
