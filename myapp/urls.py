from django.conf.urls import url
from django.urls import path

from . import views

app_name = "myapp"

urlpatterns = [
    path('form/',
         views.render_pet_adopt_form,
         name="adopt_form_page"),
    url(r'^api/pets/(?P<pk>[0-9]+)$',
        views.get_delete_update_pet,
        name='get_delete_update_pet'),
    url(r'^api/pets/$',
        views.get_post_pets,
        name='get_post_pets'),
    url(r'^pets/(?P<pk>[0-9]+)$',
        views.pet_detail_view,
        name='pet_detail_view'),
    url(r'^pets/(?P<pk>[0-9]+)/thanks$',
        views.pet_adopted,
        name='pet_adopted'),
    url(r'^pets/$',
        views.pet_gallery_view,
        name='pet_gallery_view'),
    url(r'^$',
        views.pet_gallery_view,
        name='pet_gallery_view'),
]
