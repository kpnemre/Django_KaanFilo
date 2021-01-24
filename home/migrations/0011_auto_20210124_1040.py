# Generated by Django 3.1.5 on 2021-01-24 07:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.CharField(max_length=150, verbose_name="Google'da çıkacak olan yazı")),
                ('keywords', models.CharField(max_length=150, verbose_name="Google'da aramalarda çıkabilmek için gerekli anahtar kelimler")),
                ('image', models.ImageField(upload_to='setting/', verbose_name='Ana sayfadaki büyük resim')),
                ('youtube_url', models.URLField(verbose_name='anasayfadaki URL adresi')),
                ('header', models.CharField(blank=True, max_length=150, verbose_name='ana sayfadaki resim üstündeki başlık')),
                ('content', models.CharField(blank=True, max_length=150, verbose_name='ana sayfadaki resim üsütündeki içerik')),
                ('get_startted', models.CharField(default='Get Started', max_length=50, verbose_name='Navbardaki get_started')),
                ('about', ckeditor.fields.RichTextField()),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('copyright_name', models.CharField(default='Sofistech', max_length=50)),
                ('adress', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('features', models.BooleanField(default=False, verbose_name='Özellikler kısmının gözükmesini istiyorsanız tıklayınız:')),
                ('testimonials', models.BooleanField(default=False, verbose_name='Müşteri yorumlarının sergilenmesi için tıklayınız.')),
                ('teams', models.BooleanField(default=False, verbose_name='Sofistech ekibinin segilenmesi için tıklayınız.')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='copyright_name',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='email',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='skype_url',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='twitter_url',
        ),
    ]
