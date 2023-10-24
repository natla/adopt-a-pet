from django.contrib import admin

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_per_page = 20

    list_display = ['name', 'gender', 'age', 'species', 'breed']
