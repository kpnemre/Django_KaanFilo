# Generated by Django 3.1.5 on 2021-01-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_setting_whatsapp_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='favicon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Favicon resim'),
        ),
    ]
