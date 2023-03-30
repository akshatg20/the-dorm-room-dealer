# Generated by Django 3.0.3 on 2023-03-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20230308_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='long_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='short_description',
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.IntegerField(null=True),
        ),
    ]