from django.contrib import admin
from .models import Slider

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
		
	list_display = ["slug",'title', 'content','image', 'active']
	list_editable = [ "title", 'content','image', 'active']
 
 
admin.site.register(Slider, SliderAdmin)