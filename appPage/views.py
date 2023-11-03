from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.text import slugify
from .models import *
from .forms import *
from appProduct.models import *


def index(request):
    context = dict()
    context['carousel'] = Carousel.objects.filter(
        status=True).exclude(cover_image="")
    # context['categories'] = Category.objects.filter(status = True).order_by('row_number')
    # context['subcategories'] = SubCategory.objects.filter(status = True).order_by('row_number')
    context['products'] = Product.objects.filter(is_home=True, status=True)
    return render(request, 'home/index.html', context)


def page_all(request, page_slug):
    context = dict()
    context['page'] = get_object_or_404(Page, slug=page_slug)
    context['page_title'] = f"~ {context['page'].title}"

    return render(request, 'pages/page.html', context)

