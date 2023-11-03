from django.contrib import admin
from .models import *
from django import forms
from django.utils.html import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'cover_image',
        'status',
        'row_number',
        'created_at',
        'updated_at')
    list_display_links = ['title']
    list_filter = ("status",)
    list_editable = ("status", "row_number")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'top_category',
        'row_number',
        'status')
    list_display_links = ['title']
    list_editable = ("status", "row_number")
    list_filter = ("top_category",)

    def get_subcategory_queryset(self, request):
        return super().get_queryset(request).order_by(
            "top_category__row_number", "row_number"
        )


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = SubCategory.objects.filter(status=True).select_related(
            "top_category").order_by('top_category__row_number', 'row_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = (
        'pk',
        'title',
        # 'cover_image',
        'product_image_thumbnail',
        'category_and_subcategory',
        'price',
        'stock',
        'is_home',
        'status',
        'updated_at'
    )
    list_display_links = ['title']

    prepopulated_fields = {"slug": ("title",)}
    list_filter = (
        'status',
        'category',
    )
    list_editable = ("status", "is_home")
    filter_horizontal = ("subcategory",)
    search_fields = ['title']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subcategory":
            kwargs["queryset"] = SubCategory.objects.filter(
                status=True).select_related("top_category")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def category_and_subcategory(self, obj):
        return obj.category_and_subcategory()
    category_and_subcategory.short_description = 'Kategori - Alt Kategori'

    def product_image_thumbnail(self, obj):
        if obj.cover_image:
            return mark_safe('<a href="{}"><img src="{}" width="50" height="50" /></a>'.format(obj.cover_image.url, obj.cover_image.url))
        else:
            return "Resim Yok"
    product_image_thumbnail.short_description = 'Ürün resmi'
