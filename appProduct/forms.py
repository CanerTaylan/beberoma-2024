from django import forms
from .models import *


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

