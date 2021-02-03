from django.contrib.sitemaps import Sitemap
from django.urls import reverse


from .models import Blog


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home:home', 'home:offer']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Blog.objects.filter(active = True)