from django.shortcuts import render
from app.models import Products


def products_list(request):
    products = Products.objects.all()
    context = {
        "products_list": products,
    }
    return render(
        request,
        template_name="myapp/products_list.html",
        context=context,  
    )


def get_products_by_id(request, product_id):
    products = Products.objects.get(id=product_id)
    context = {
        "products": products,

    }

    return render(
        request, 
        template_name: "app/product_detals.html",
        context=context

    )






def products_detail(request):
    # Логіка для відображення деталей продукту
    pass