# Generated by Django 4.1 on 2022-12-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_description_alter_product_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(),
        ),
    ]
