# Generated by Django 3.1.2 on 2020-10-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomizer',
            name='word1',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomizer',
            name='word2',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomizer',
            name='word3',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomizer',
            name='word4',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomizer',
            name='word5',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomizer',
            name='word6',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomizer',
            name='word7',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomizer',
            name='word81',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomizer',
            name='word82',
            field=models.CharField(default='empty', max_length=30),
            preserve_default=False,
        ),
    ]
