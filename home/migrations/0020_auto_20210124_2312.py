# Generated by Django 3.1.5 on 2021-01-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210124_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='content',
            field=models.TextField(verbose_name='Hakkımızda kısmı için içerik:'),
        ),
    ]