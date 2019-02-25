"""my_django21_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from myapp import views
from django.contrib.sitemaps.views import sitemap
from myapp.sitemaps import PostSitemap

# Create a sitemaps dictionary:
sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    url(r'blog/', include('myapp.urls', namespace='myapp')),
    path('blog/', views.post_detail_view, name="blog_home"),
    path('blog/bios.html/', views.sim_bios, name='sim_bios'),
    path('blog/contact.html/', views.blog_contact, name='blog_contact'),
    path('admin/', admin.site.urls),
    path('index/', views.offer_list, name="home_page"),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	url(r'^$', views.post_list_view, name='post_list_view'),
]
