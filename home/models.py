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

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'slug':self.slug})

                                                                                                                                                                                                                                                                                