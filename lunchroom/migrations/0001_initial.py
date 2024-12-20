# Generated by Django 5.1.3 on 2024-11-17 12:10

import django.db.models.deletion
import mptt.fields
import versatileimagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=255, null=True, unique=True, verbose_name='name')),
                ('name_ka', models.CharField(max_length=255, null=True, unique=True, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='dish/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'dish',
                'verbose_name_plural': 'dishes',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='name')),
                ('name_ka', models.CharField(max_length=255, null=True, verbose_name='name')),
                ('dish', models.ManyToManyField(related_name='ingredients', to='lunchroom.dish', verbose_name='dish')),
            ],
            options={
                'verbose_name': 'ingredient',
                'verbose_name_plural': 'ingredients',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=40, null=True, unique=True, verbose_name='name')),
                ('name_ka', models.CharField(max_length=40, null=True, unique=True, verbose_name='name')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='menu_category/', verbose_name='image')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='lunchroom.menu', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menues',
            },
        ),
        migrations.AddField(
            model_name='dish',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='lunchroom.menu', verbose_name='menu'),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=40, null=True, unique=True, verbose_name='name')),
                ('name_ka', models.CharField(max_length=40, null=True, unique=True, verbose_name='name')),
                ('address', models.CharField(max_length=150, unique=True, verbose_name='address')),
                ('address_en', models.CharField(max_length=150, null=True, unique=True, verbose_name='address')),
                ('address_ka', models.CharField(max_length=150, null=True, unique=True, verbose_name='address')),
                ('phone_number', models.CharField(max_length=15, unique=True, verbose_name='phone_number')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='restaurant/', verbose_name='image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'restaurant',
                'verbose_name_plural': 'restaurants',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='lunchroom.restaurant', verbose_name='restaurant'),
        ),
    ]
