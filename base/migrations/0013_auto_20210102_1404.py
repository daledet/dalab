# Generated by Django 3.1.4 on 2021-01-02 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20210102_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='catagory',
            new_name='category',
        ),
    ]