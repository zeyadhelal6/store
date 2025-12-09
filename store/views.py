from django.shortcuts import render

def allproducts(request):
    return render(request, 'products.html')

