# Generated by Django 3.1.2 on 2020-10-20 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20201020_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='author',
        ),
    ]
