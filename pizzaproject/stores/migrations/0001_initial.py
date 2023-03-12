# Generated by Django 4.1.3 on 2023-02-04 22:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzera_name', models.CharField(max_length=100)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.IntegerField(blank=True, default=0)),
                ('website', models.URLField(blank=True)),
                ('phone_number', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex='^\\1?\\d{9,10}$')])),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=245)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]