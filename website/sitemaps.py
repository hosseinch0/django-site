from django.contrib import sitemaps
from django.urls import reverse 


class StaticViewSitemaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    

    def items(self):
        return ['website:index', 'website:about', 'website:contact']


    def location(self, item):
        return reverse(item)