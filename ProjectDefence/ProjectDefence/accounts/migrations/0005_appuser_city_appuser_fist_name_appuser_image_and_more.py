# Generated by Django 4.1 on 2022-12-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='city',
            field=models.CharField(default='plovdiv', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='fist_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='street',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
