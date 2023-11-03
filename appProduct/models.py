from django.db import models
from appPage.models import DEFAULT_STATUS, STATUS
from django.utils.text import slugify
from django.urls import reverse


# * ana kategori
# ? pk
# ? title
# ? pozisyon
# ? status
# * sub kategori
# ? pk
# ? title
# ? pozisyon
# ? status
# * ürünler
# ? pk
# ? image
# ? title
# ? kategori,subkategori
# ? fiyat
# ? stok
# ? status
# + açıklama
# + renk
# + beden
# + ayakkabı numarası


class Category(models.Model):
    title = models.CharField(("Kategori Adı "), max_length=50)
    slug = models.SlugField(("Slug"), max_length=200, null=True, blank=True)
    cover_image = models.ImageField(
        ('Kategori Resmi '),
        upload_to='category',
        null=True,
        blank=True,)
    status = models.BooleanField("Aktif | Pasif", default=True)
    row_number = models.PositiveIntegerField(("Sıra "), default=1)              
    created_at = models.DateTimeField(("Oluştuma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(("Güncelleme Tarihi"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            last_category = Category.objects.order_by('-row_number').first()
            if last_category:
                self.row_number = last_category.row_number + 1
        if not self.slug or self.title != self._meta.get_field('title').default:
            self.slug = slugify(self.title.replace('ı', 'i'))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ('row_number',)


class SubCategory(models.Model):
    title = models.CharField(("Alt Kategori Adı "), max_length=50)
    top_category = models.ForeignKey("Category", verbose_name=(
        "Ana Kategori"), on_delete=models.CASCADE, default="-")
    slug = models.SlugField(("Slug"), max_length=200, null=True, blank=True)
    status = models.BooleanField("Aktif | Pasif", default=True)
    row_number = models.PositiveIntegerField(("Sıra "), default=1)
    created_at = models.DateTimeField(("Oluştuma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(("Güncelleme Tarihi"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            related_subcategories = SubCategory.objects.filter(
                top_category=self.top_category)
            top_number_of_row = related_subcategories.order_by(
                '-row_number').first()
            if top_number_of_row is None:
                self.row_number = 1
            else:
                self.row_number = top_number_of_row.row_number + 1
        if not self.slug or self.title != self._meta.get_field('title').default:
            self.slug = slugify(self.title.replace('ı', 'i'))
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f"{1000 + self.pk} - {self.top_category.title} - {self.title}"

    class Meta:
        verbose_name = "Alt Kategori"
        verbose_name_plural = "Alt Kategoriler"
        ordering = ('top_category__row_number', 'row_number')


class Product(models.Model):
    category = models.ManyToManyField("Category", verbose_name=(
        "Kategori"))
    subcategory = models.ManyToManyField("SubCategory", verbose_name=(
        "Alt Kategori"),)
    title = models.CharField(("Ürün Adı "), max_length=50)
    slug = models.SlugField(
        max_length=50,
        default="",
    )
    content = models.TextField(("İçerik"), max_length=500000,)
    cover_image = models.ImageField(
        ('Ürün Resmi '),
        upload_to='product',
        null=True,
        blank=True,)
    old_price = models.DecimalField(
        ("EskiFiyat"), max_digits=6, decimal_places=2, default=0)
    price = models.DecimalField(("Fiyat"), max_digits=6, decimal_places=2)
    stock = models.PositiveSmallIntegerField(("Stok"), default=0)
    status = models.BooleanField(("Aktif"), default=False)
    is_home = models.BooleanField(("Anasayfada"), default=False)
    created_at = models.DateTimeField(("Oluştuma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(("Güncelleme Tarihi"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self._meta.get_field('title').default:
            self.slug = slugify(self.title.replace('ı', 'i'))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def category_and_subcategory(self):
        subcategory_info = " | ".join(
            [f"{subcategory.top_category.title} - {subcategory.title}" for subcategory in self.subcategory.all()])
        return subcategory_info

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
