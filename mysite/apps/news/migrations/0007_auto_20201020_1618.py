# Generated by Django 3.1.2 on 2020-10-20 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='User',
            new_name='author',
        ),
    ]