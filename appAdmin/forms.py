from django import forms
from appProduct.models import *
from appPage.models import *


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =[
            'title',
            'cover_image',
            'row_number',
            'status',
            'slug',
        ]


class SubCategoryModelForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields =[
            'title',
            'top_category',
            'status',
            'row_number',
            'slug',
        ]

class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields =[
            'title',
            'cover_image',
            'row',
            'status',
        ]
       # fields = '__all__'
       # exclude =['title']

class PageModelForm(forms.ModelForm):
    class Meta:
        model = Page
        fields =[
            'title',
            'slug',
            'cover_image',
            'content',
            'status',
        ]

