# Generated by Django 3.1.5 on 2021-01-22 20:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_blog_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
    ]
