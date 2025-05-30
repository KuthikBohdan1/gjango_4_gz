from django.shortcuts import render
from app.models import Products


def product_list(request):
    products = Products.objects.all()
    context = {
        "products_list": products,
    }
    return render(
        request,
        template_name="myapp/products_list.html",
        context=context,  
    )