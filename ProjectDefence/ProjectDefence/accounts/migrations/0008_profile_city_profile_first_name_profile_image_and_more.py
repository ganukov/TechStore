# Generated by Django 4.1 on 2022-12-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_city_remove_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='london', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Georgi', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Ganukov', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='street',
            field=models.CharField(default='269b Staines road', max_length=25),
            preserve_default=False,
        ),
    ]
