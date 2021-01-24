from django.contrib import admin
from .models import Slider, Blog, Offer, ContactInfo, Setting, Car

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
		
	list_display = ["slug",'title', 'content','image', 'active']
	list_editable = [ "title", 'content','image', 'active']
 
class BlogAdmin(admin.ModelAdmin):
		
	list_display = ["slug",'title','image', 'active', "about"]
	list_editable = [ "title", 'image', 'active', "about"]
 
class OfferAdmin(admin.ModelAdmin):
		
	list_display = ["name",'surname', 'company','email', 'number', "city","number_of_car","renting_time","message"]

class ContactAdmin(admin.ModelAdmin):
		
	list_display = ["name"]
 
class SettingAdmin(admin.ModelAdmin):
		
	list_display = ["title","description","keywords","facebook_url","twitter_url","instagram_url","linkedin_url","copyright_name","adress","email","phone", "phone2"]

class CarAdmin(admin.ModelAdmin):
		
	list_display = ["name"]

admin.site.register(Car, CarAdmin)
admin.site.register(ContactInfo, ContactAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Setting, SettingAdmin)