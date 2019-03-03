from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index/',
         views.render_pet_adopt_form,
         name="home_page"),
    url(
        r'^api/pets/(?P<pk>[0-9]+)$',
        views.get_delete_update_pet,
        name='get_delete_update_pet'
    ),
    url(
        r'^api/pets/$',
        views.get_post_pets,
        name='get_post_pets'
    ),
    url(r'^$',
        views.render_pet_adopt_form,
        name='home_page'),
]
