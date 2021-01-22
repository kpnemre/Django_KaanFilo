from django.contrib import admin
from .models import Slider, Blog

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
		
	list_display = ["slug",'title', 'content','image', 'active']
	list_editable = [ "title", 'content','image', 'active']
 
class BlogAdmin(admin.ModelAdmin):
		
	list_display = ["slug",'title', 'content','image', 'active', "about"]
	list_editable = [ "title", 'content','image', 'active', "about"]
 
admin.site.register(Slider, SliderAdmin)
admin.site.register(Blog, BlogAdmin)