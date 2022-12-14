# Generated by Django 4.1 on 2022-12-12 14:40

import ProjectDefence.accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_appuser_city_remove_appuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.IntegerField(default=269, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[ProjectDefence.accounts.validators.check_name_contains_only_letters, django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[ProjectDefence.accounts.validators.check_name_contains_only_letters, django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
