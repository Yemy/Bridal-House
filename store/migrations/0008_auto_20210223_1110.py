# Generated by Django 2.2.7 on 2021-02-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210223_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrating',
            name='rating',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='', max_length=1),
        ),
    ]
