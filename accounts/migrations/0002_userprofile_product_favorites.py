# Generated by Django 4.0 on 2024-05-12 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options_and_more'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='product_favorites',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
