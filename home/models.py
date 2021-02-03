from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from ckeditor.fields import RichTextField

# Create your models here.

class Slider(models.Model):
    title = models.CharField("Başlık", max_length=100, unique = True)
    image = models.ImageField("Resim", blank=True,null=True)
    created_date = models.DateTimeField("Oluşturma zamanı", auto_now_add=True)
    content= models.CharField("İçerik", max_length=200)
    slug = models.SlugField(editable = False)
    active = models.BooleanField("Sitede gösterilsin mi?", default = False)
    
    
        
    class Meta:
        verbose_name = 'Slayt'
        verbose_name_plural = 'Slaytlar'
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Slider, self).save(*args, **kwargs)

    #def get_absolute_url(self):
        #return reverse('home:detail', kwargs={'slug':self.slug})

class Blog(models.Model):
    FEATURE_FONTS = (
        ("icofont-auto-mobile", "araba"),
        ("icofont-automation", "hizmetler"),
        ("icofont-bullseye", "avantaj"),
        ("ri-store-line", "dükkan"),
    )

    font_title = models.CharField("Font Başlık", max_length=50)
    font = models.CharField(max_length=50, choices=FEATURE_FONTS)
    title = models.CharField("Başlık", max_length=100, unique = True)
    sub_content = models.CharField("Kısa İçerik", max_length=100)
    image = models.ImageField("Resim", blank=True,null=True)
    created_date = models.DateTimeField("Oluşturma zamanı", auto_now_add=True)
    content= RichTextField("İçerik")
    slug = models.SlugField(editable = False)
    active = models.BooleanField("Sitede gösterilsin mi?", default = False)
    about = models.BooleanField("Neden Kiralama Başlığı için tıklayınız", default = False)
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150, default ="Kaanfilo")
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150, default = "Kaan Filo, araç kiralama")  
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
        # ordering = ['sıralama']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'slug':self.slug})


class Offer(models.Model):
    name = models.CharField("İsim Soy:", max_length = 30)
    surname = models.CharField("Soyad:", max_length = 30)
    company = models.CharField("Firma:", max_length = 70)
    email = models.EmailField("Eposta adresi:")
    number = models.SmallIntegerField("Telefon Numaranız:")
    city = models.CharField("Şehir", max_length = 30)
    number_of_car = models.SmallIntegerField("Kiralanacak Araç Sayısı:")
    renting_time = models.SmallIntegerField("Kiralanacak Gün Sayısı:")
    message = models.TextField("Mesajınız:")

    class Meta:
        verbose_name = 'Teklif'
        verbose_name_plural = 'Teklifler'
    
    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    name = models.CharField("İsminiz:", max_length=40)
    email = models.EmailField("Email:")
    topic = models.CharField("Konu:", max_length = 150)
    content = models.TextField("Mesajınız:")

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Gelen Mesaj'
        verbose_name_plural = 'Gelen Mesajlar'

    def __str__(self):
        return self.name

class Setting(models.Model):
    title = models.CharField("title", max_length=50)
    description = models.CharField("Google'da çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)   
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    copyright_name = models.CharField(max_length=50, default="KaanFilo")
    adress = models.CharField(max_length=75)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    whatsapp_phone = models.CharField(max_length=20)
    image = models.ImageField("Hakkımızda kısmı için resim", blank=True, null=True)
    content = models.TextField("Hakkımızda kısmı için içerik:")
    favicon = models.ImageField("Favicon resim", blank=True, null=True)
    

    



    class Meta:
        verbose_name = 'Ayar'
        verbose_name_plural = 'Ayarlar'
    def __str__(self):
        return self.title


class Car(models.Model):
    name = models.CharField("Arabanın ismi", max_length = 50)
    image = models.ImageField("Resim", blank=True, null=True)
    price = models.SmallIntegerField("Fiyat", default = 0)

    def __str__(self):
        return self.name



                                                                                                                                                                                                                                                                                