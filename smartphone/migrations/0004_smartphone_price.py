# Generated by Django 3.2.25 on 2024-11-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0003_smartphone_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
