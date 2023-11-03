from django.urls import path
from .views import *


urlpatterns = [



    path('<slug:page_slug>', page_all, name='page_all'),

]
