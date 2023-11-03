from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.text import slugify
from .models import *
from .forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import DetailView


def all_products(request, category_slug, subcategory_pk=None, subcategory_slug=None):
    context = dict()
    context['category'] = get_object_or_404(Category, slug=category_slug)
    context['categories'] = Category.objects.filter(status=True)
    context['subcategories'] = SubCategory.objects.filter(status=True)
    if subcategory_slug is None and subcategory_pk is None:

        context['products'] = Product.objects.filter(
            category=context['category'],
            status=True,
            stock__gte=1,       # gte eşit ve daha büyük anlamına geliyor
        )
        context['page_title'] = f"~ {context['category'].title}"
    else:

        context['subcategory'] = get_object_or_404(
            SubCategory, pk=subcategory_pk, slug=subcategory_slug)
        context['products'] = Product.objects.filter(
            category=context['category'],
            subcategory=context['subcategory'],
            status=True,
            stock__gte=1,
        )
        context['page_title'] = f"~ {context['subcategory'].title}"
    return render(request, 'product/category.html', context)


# def product_details(request, category_slug, product_pk, product_slug):
#     context=dict()
#     context['category'] = get_object_or_404(Category, slug=category_slug)
#     product_id = product_pk + 1000
#     context['product'] = get_object_or_404(Product, pk=product_id, slug=product_slug)
#     context['page_title'] = f"~ {context['product'].title.title()}"

#     return render(request, 'product/product_details.html', context)

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'product/product_detail.html'


def product_details(request, category_slug, product_slug):
    context = dict()
    context['category'] = get_object_or_404(Category, slug=category_slug)

    context['product'] = get_object_or_404(Product, slug=product_slug)

    context['page_title'] = f"~ {context['product'].title.title()}"

    return render(request, 'product/product_details.html', context)


# class ProductDetailView(DetailView):

#     model = Product
#     template_name = 'product/product_details.html'
