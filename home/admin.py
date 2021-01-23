from django.contrib import admin
from .models import Slider, Blog, Offer, ContactInfo

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
		
	list_display = ["slug",'title', 'content','image', 'active']
	list_editable = [ "title", 'content','image', 'active']
 
class BlogAdmin(admin.ModelAdmin):
		
	list_display = ["slug",'title', 'content','image', 'active', "about"]
	list_editable = [ "title", 'image', 'active', "about"]
 
class OfferAdmin(admin.ModelAdmin):
		
	list_display = ["name",'surname', 'company','email', 'number', "city","number_of_car","renting_time","message"]

class ContactAdmin(admin.ModelAdmin):
		
	list_display = ["name"]

admin.site.register(ContactInfo, ContactAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Offer, OfferAdmin)