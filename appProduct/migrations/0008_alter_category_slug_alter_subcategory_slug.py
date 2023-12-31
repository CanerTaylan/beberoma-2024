# Generated by Django 4.2.2 on 2023-09-26 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProduct', '0007_product_subcategory_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=200, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default='', max_length=200, null=True, verbose_name='Slug'),
        ),
    ]
