# Generated by Django 3.1.5 on 2021-01-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_blog_sub_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Arabanın ismi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Resim')),
                ('price', models.SmallIntegerField(default=0, verbose_name='Fiyat')),
            ],
        ),
    ]
