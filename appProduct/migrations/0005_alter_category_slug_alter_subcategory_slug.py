# Generated by Django 4.2.2 on 2023-09-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProduct', '0004_alter_category_slug_alter_subcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
