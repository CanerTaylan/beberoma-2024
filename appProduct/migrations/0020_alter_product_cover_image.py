# Generated by Django 4.2.2 on 2023-10-08 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProduct', '0019_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='product', verbose_name='Ürün Resmi '),
        ),
    ]
