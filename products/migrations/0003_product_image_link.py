# Generated by Django 4.0.4 on 2022-04-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_car_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_link',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]
