from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from . models import Product
from . forms import ProductForm
# Create your views here.
def home_view(request):
    return render(request, "products/start_page.html",{"title":"home page"})
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
    "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {"object":obj}
    return render(request, 'products/product_delete.html',context)

def product_detail_view(request):
    obj = Product.objects.get(id=6)
#    context = {
#    'title': obj.title,
#    'description': obj.description
#    }
    context = {"object":obj}
    return render(request,"products/detail.html",context)

def dynamic_lookup_view(request,my_id):
    obj = get_object_or_404(Product,id=my_id)
    context = {"object":obj}
    return render(request,"products/detail.html",context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        #return HttpResponseRedirect("../products/product_list_view")

    print(request.POST)
    context = {
        "form":form
    }
    return render(request,"products/product_create.html",context)
