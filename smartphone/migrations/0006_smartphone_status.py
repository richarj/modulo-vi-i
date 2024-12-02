# Generated by Django 3.2.25 on 2024-11-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0005_book_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='status',
            field=models.CharField(choices=[('disponible', 'Disponible'), ('agotado', 'Agotado')], default='disponible', max_length=15),
        ),
    ]
