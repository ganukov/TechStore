# Generated by Django 4.1 on 2022-12-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_specifications_product_cpu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(),
        ),
    ]
