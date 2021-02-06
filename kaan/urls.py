"""kaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from home.sitemaps import BlogSitemap, StaticViewSitemap


sitemaps = {
	'blogs' : BlogSitemap,
    'static': StaticViewSitemap,

}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type ="text/plain")),   
    path('google42bbd82ce6dc94c4.html/', TemplateView.as_view(template_name="google42bbd82ce6dc94c4.html", content_type ="text/plain")),   
    path('yandex_5f9e6d82bf483a38.html/', TemplateView.as_view(template_name="yandex_5f9e6d82bf483a38.html", content_type ="text/plain")),   
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
