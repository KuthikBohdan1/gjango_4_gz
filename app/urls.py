from django.urls import path
from app import views as app_views

urlpatterns = [
    path("admin/", app_views.product_list, name="product_list"),
    path("products/", app_views.product_detail, name="product_detail"),
]