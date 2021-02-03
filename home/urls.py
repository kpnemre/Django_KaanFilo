from django.urls import path
from . import views


app_name = "home"
urlpatterns = [
    path('', views.home, name= "home"),
    path('teklif-al/', views.offer, name= "offer"),
    #path('iletisim/', views.contact, name= "contact"),
    path('<slug:slug>/', views.blog_detail, name= "detail"),
    # path('about/', views.about, name= "about"),
]