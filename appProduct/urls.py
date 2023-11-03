from django.urls import path
from .views import *
from appAdmin.views import *


urlpatterns = [
    path('<slug:category_slug>/', all_products, name='category_all'),
    path('<slug:category_slug>/<int:subcategory_pk>-<slug:subcategory_slug>/', all_products, name='subcategory_all'),
    path('<slug:category_slug>/<slug:product_slug>', product_details, name='product_details'),


]
