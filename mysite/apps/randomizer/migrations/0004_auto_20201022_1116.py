# Generated by Django 3.1.2 on 2020-10-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0003_auto_20201020_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item81',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item82',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='item1',
            old_name='word',
            new_name='item',
        ),
    ]
