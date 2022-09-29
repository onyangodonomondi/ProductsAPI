from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
# def product(request,product_id):
#     product = Product.objects.get(pk=product_id)
#     if product is not None:
#         return render(request,'inventory/product.html',{'product':product})
 
#     else:
#         return HttpResponse('Product not found')
def product(request):
    products = Product.objects.all()
    return render(request,'inventory/product.html',{'products':products})