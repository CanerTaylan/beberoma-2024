from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from .models import *
from .forms import *
from appProduct.models import *
from appPage.models import *


def admin_index(request):
    context = dict()
    context['page_title'] = "AnaSayfa"

    return render(request, 'admin_paneli/admin.html', context)

# product


def category(request):
    context = dict()
    context['category'] = Category.objects.all().order_by('row_number')
    context['page_title'] = "Kategoriler"

    return render(request, 'admin_paneli/category.html', context)


def category_create(request):
    context = dict()
    context['page_title'] = "Kategori Ekle"
    context['title'] = "Kategori Ekle"
    context['form'] = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(category.title.replace('ı', 'i'))
            category.save()
            messages.success(request, 'Kategori eklendi')
            return redirect('category')
    return render(request, 'admin_paneli/form.html', context)


def category_update(request, pk):
    context = dict()
    context['page_title'] = "Kategori Güncelle"
    category = Category.objects.get(pk=pk)
    context['title'] = "Kategori Güncelle"
    context['sub_title'] = f"{category.title}"
    context['form'] = CategoryModelForm(instance=category)
    if request.method == "POST":
        form = CategoryModelForm(
            request.POST, request.FILES, instance=category)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
            messages.success(request, "Kategori güncellendi.")
            return redirect('category')
    return render(request, 'admin_paneli/form.html', context)


def category_delete(request, pk):
    item = Category.objects.get(pk=pk)
    item.status = False
    item.save()
    messages.warning(request, "Kategori pasif yapıldı.")
    return redirect('category')


def subcategory(request):
    context = dict()
    context['page_title'] = "Alt Kategoriler"
    context['subcategory'] = SubCategory.objects.all().order_by(
        'top_category__row_number', 'row_number')

    return render(request, 'admin_paneli/subcategory.html', context)


def subcategory_create(request):
    context = dict()
    context['page_title'] = "Alt Kategori Ekle"
    context['title'] = "Alt Kategori Ekle"
    context['form'] = SubCategoryModelForm()
    if request.method == 'POST':
        form = SubCategoryModelForm(request.POST, request.FILES)

        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.slug = slugify(subcategory.title.replace('ı', 'i'))
            subcategory.save()
            messages.success(request, 'Alt Kategori eklendi')
            if 'return_list' in request.POST:
                return redirect('subcategory')
            elif 'add_new' in request.POST:
                return redirect('subcategory_create')
    return render(request, 'admin_paneli/form.html', context)


def subcategory_update(request, pk):
    context = dict()
    context['page_title'] = "Alt Kategori Güncelle"
    subcategory = SubCategory.objects.get(pk=pk)
    context['title'] = "Alt Kategori Güncelle"
    context['subtitle'] = f"{subcategory.title}"
    context['form'] = SubCategoryModelForm(instance=subcategory)
    if request.method == "POST":
        form = SubCategoryModelForm(request.POST, instance=subcategory)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
            messages.success(request, "Alt Kategori güncellendi.")
            if 'return_list' in request.POST:
                return redirect('subcategory')
            elif 'add_new' in request.POST:
                return redirect('subcategory_create')
    return render(request, "admin_paneli/form.html", context)


def subcategory_delete(request, pk):
    item = SubCategory.objects.get(pk=pk)
    item.status = False
    item.save()
    messages.warning(request, "Alt kategori pasif yapıldı.")
    return redirect('subcategory')


# Sayfa

def page_list(request):
    context = dict()
    context['page_title'] = "Sayfa listesi"
    context['pages'] = Page.objects.all().order_by('-pk')
    return render(request, 'admin_paneli/page_list.html', context)


def page_create(request):
    context = dict()
    context['page_title'] = "Sayfa Ekle"
    context['title'] = "Sayfa Ekleme Formu"
    context['form'] = PageModelForm()

    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            # ? (formu kaydeti item a eşitledik ve kaydetmeyi durdur)
            item = form.save(commit=False)
            # ? item slug'ını oluşturduk. ı yı bazen i yapmamasından dolayı ayrı olarak beliritiyoruz
            item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()  # ? item yani formu kaydettik
            messages.success(request, 'Sayfa eklendi')
            return redirect('page_list')
    return render(request, 'admin_paneli/form.html', context)


def page_update(request, pk):
    context = dict()
    context['page_title'] = "Sayfa Güncelle"
    pages = Page.objects.get(pk=pk)
    context['title'] = f"{pages.title} sayfası düzenleniyor."
    context['form'] = PageModelForm(instance=pages)
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES, instance=pages)
        if form.is_valid():
            # ? save yapmadan geçici nesne oluşturur. slug ilave eder ve sonra kaydeder
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace('ı', 'i'))
            item.save()
            messages.success(request, 'Sayfa güncellendi.')
            return redirect('page_list')
    return render(request, 'admin_paneli/form.html', context)


def page_delete(request, pk):
    item = Page.objects.get(pk=pk)
    item.status = "DEL"
    item.save()
    messages.warning(request, 'Sayfa "Silindi" olarak işaretlendi.')

    return redirect('page_list')


# carousel

def carousel_list(request):
    context = dict()
    context['page_title'] = "Slayt listesi"
    context['carousel'] = Carousel.objects.all().order_by('-row')
    return render(request, 'admin_paneli/carousel_list.html', context)


def carousel_create(request):
    context = dict()
    context['page_title'] = "Slayt Ekle"
    context['title'] = "Slayt Ekleme Formu"
    context['form'] = CarouselModelForm()

    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # carousel = Carousel.objects.create(title=request.POST.get('title'))
        messages.success(request, 'Slayt eklendi')
        return redirect('carousel_list')
    return render(request, 'admin_paneli/form.html', context)


def carousel_update(request, pk):
    context = dict()
    context['page_title'] = "Slayt Güncelle"
    slide = Carousel.objects.get(pk=pk)
    context['title'] = f"{slide.pk}-{slide.title}"
    context['form'] = CarouselModelForm(instance=slide)
    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slayt güncellendi.')
            return redirect('carousel_list')
    return render(request, 'admin_paneli/form.html', context)


def carousel_delete(request, pk):
    item = Carousel.objects.get(pk=pk)
    item.status = False
    item.save()
    messages.warning(request, 'Slayt "Pasif" olarak işaretlendi.')

    return redirect('carousel_list')
