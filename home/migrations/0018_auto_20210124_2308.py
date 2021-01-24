# Generated by Django 3.1.5 on 2021-01-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_setting_phone2'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='content',
            field=models.CharField(default=1, max_length=350, verbose_name='Hakkımızda kısmı için içerik:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Hakkımızda kısmı için resim'),
        ),
    ]
