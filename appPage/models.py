from django.db import models
from django.utils.text import slugify


DEFAULT_PAGE_STATUS = "DRF"
PAGE_STATUS = [
    # + left side : DB
    # + right side : human-readable
    ("DRF", "Taslak"),
    ("PSH", "Yayınlandı"),
    ("DEL", "Silindi"),
]
DEFAULT_STATUS = "AKTF"
STATUS = [
    ("PSF", "Pasif"),
    ("AKTF", "Aktif")
]


class Page(models.Model):
    title = models.CharField(("Sayfa Adı"), max_length=200)
    slug = models.SlugField(("Slug"), max_length=200, default="")

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self._meta.get_field('title').default:
            self.slug = slugify(self.title.replace('ı', 'i'))

        super(Page, self).save(*args, **kwargs)

    content = models.TextField(("İçerik"), max_length=500000,)
    cover_image = models.ImageField(
        ("Resim"),
        upload_to='page',
        null=True,
        blank=True)
    status = models.CharField(
        ("Status"),
        default=DEFAULT_PAGE_STATUS,
        choices=PAGE_STATUS,
        max_length=10)
    created_at = models.DateTimeField(("Oluştuma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(("Güncelleme Tarihi"), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sayfa"
        verbose_name_plural = "Sayfalar"


class Carousel(models.Model):
    title = models.CharField(
        ("Başlık "), max_length=50, blank=True, null=True,)
    cover_image = models.ImageField(
        ('Slayt Resmi '),
        upload_to='carousel',
        null=True,
        blank=True,)
    row = models.PositiveIntegerField(("Sıra "), default=1)

    def save(self, *args, **kwargs):
        if not self.pk:
            last_slide = Carousel.objects.order_by('-row').first()
            if last_slide:
                self.row = last_slide.row + 1
        super(Carousel, self).save(*args, **kwargs)
    status = models.BooleanField("Aktif | Pasif", default=True)
    created_at = models.DateTimeField(("Oluştuma Tarihi"), auto_now_add=True)
    updated_at = models.DateTimeField(("Güncelleme Tarihi"), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slayt"
        verbose_name_plural = "Slaytlar"
