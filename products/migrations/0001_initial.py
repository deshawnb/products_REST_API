# Generated by Django 4.0.4 on 2022-04-13 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('inventory_quantity', models.IntegerField()),
            ],
        ),
    ]
