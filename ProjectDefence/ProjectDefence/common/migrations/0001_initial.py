# Generated by Django 4.1 on 2022-12-16 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=25)),
                ('subject', models.CharField(max_length=15)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
