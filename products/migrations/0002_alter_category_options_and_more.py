# Generated by Django 5.0.4 on 2024-05-03 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_url',
            new_name='image',
        ),
    ]
