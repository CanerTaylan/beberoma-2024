from django.contrib import admin
from .models import *
from django.utils.html import mark_safe


# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'status','updated_at')
    list_display_links = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status",)
    list_editable =("status",)

    def __str__(self):
        return self.title



@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('pk', 'row','title', 'slide_thumbnail','status', 'updated_at')
    list_editable =("row","status")

    def slide_thumbnail(self, obj):
        if obj.cover_image:
            return mark_safe('<a href="{}"><img src="{}" width="150" height="50" /></a>'.format(obj.cover_image.url, obj.cover_image.url))
        else:
            return "Resim Yok"
    slide_thumbnail.short_description = 'Slayt'
    
    def __str__(self):
        return self.title
