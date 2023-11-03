# Generated by Django 4.2.2 on 2023-10-04 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appProduct', '0017_alter_category_options_remove_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appProduct.category', verbose_name='Kategori'),
        ),
    ]
