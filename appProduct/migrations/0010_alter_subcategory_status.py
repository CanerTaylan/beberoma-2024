# Generated by Django 4.2.2 on 2023-09-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProduct', '0009_alter_category_slug_alter_category_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
