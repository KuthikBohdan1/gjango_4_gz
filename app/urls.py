from django.urls import path
from app import views as app_views

urlpatterns = [
    path("admin/", app_views.products_list, name="products_list"),
    path("products/", app_views.products_detail, name="products_detail"), 
]