from django.shortcuts import render
from app.models import Products


def product_list(requsest):
    products = Products.objects.all()

    return render(
        request,
        template_name="myapp/products_list.html"
        context=

    )