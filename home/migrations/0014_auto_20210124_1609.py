# Generated by Django 3.1.5 on 2021-01-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210124_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='copyright_name',
            field=models.CharField(default='KaanFilo', max_length=50),
        ),
    ]
