# Generated by Django 3.1.4 on 2020-12-29 05:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20201228_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
