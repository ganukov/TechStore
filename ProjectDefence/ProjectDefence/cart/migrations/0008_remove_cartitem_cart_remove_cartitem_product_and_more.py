# Generated by Django 4.1 on 2022-12-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_remove_cart_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]