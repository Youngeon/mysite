# Generated by Django 3.1.2 on 2020-10-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0004_auto_20201022_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
    ]
