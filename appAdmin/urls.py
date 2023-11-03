from django.urls import path
from .views import *



urlpatterns = [
    path('', admin_index, name='admin_index'),
    path('carousel/list/', carousel_list, name='carousel_list'), 
    path('carousel/create/', carousel_create, name='carousel_create'), 
    path('carousel/update/<int:pk>/', carousel_update, name='carousel_update'), 
    path('carousel/delete/<int:pk>/', carousel_delete, name='carousel_delete'), 


    path('page/list/', page_list, name='page_list'), 
    path('page/create/', page_create, name='page_create'), 
    path('page/update/<int:pk>/', page_update, name='page_update'), 
    path('page/delete/<int:pk>/', page_delete, name='page_delete'), 


    path('category/', category, name='category'),
    path('category/create/', category_create, name='category_create'),
    path('category/update/<int:pk>/', category_update, name='category_update'),
    path('category/delete/<int:pk>/', category_delete, name='category_delete'),


    path('subcategory/', subcategory, name='subcategory'),
    path('subcategory/create/', subcategory_create, name='subcategory_create'),
    path('subcategory/update/<int:pk>/',
         subcategory_update, name='subcategory_update'),
    path('subcategory/delete/<int:pk>/',
         subcategory_delete, name='subcategory_delete'),    
]  