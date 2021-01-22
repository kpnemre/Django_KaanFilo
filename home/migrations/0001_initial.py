# Generated by Django 3.1.5 on 2021-01-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Başlık')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Resim')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma zamanı')),
                ('content', models.CharField(max_length=200, verbose_name='İçerik')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Slayt',
                'verbose_name_plural': 'Slaytlar',
                'ordering': ['-created_date'],
            },
        ),
    ]
