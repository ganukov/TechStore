# Generated by Django 4.1 on 2022-12-12 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_orderitem_order_alter_orderitem_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
