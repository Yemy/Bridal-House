# Generated by Django 2.2.7 on 2021-03-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210307_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True, help_text="Product Slug is a url for that Specific Product, Please Don't Edit this if you don't have to", null=True),
        ),
    ]
