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
    title = models.CharField("Başlık", max_length=100, unique = True)
    image = models.ImageField("Resim", blank=True,null=True)
    created_date = models.DateTimeField("Oluşturma zamanı", auto_now_add=True)
    content= RichTextField("İçerik")
    slug = models.SlugField(editable = False)
    active = models.BooleanField("Sitede gösterilsin mi?", default = False)
    about = models.BooleanField("Neden Kiralama Başlığı için tıklayınız", default = False)
    sıralama = models.SmallIntegerField(default = 0)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
        ordering = ['sıralama']
    
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


    class Meta:
        verbose_name = 'Ayar'
        verbose_name_plural = 'Ayarlar'
    def __str__(self):
        return self.title


                                                                                                                                                                                                                                                                                