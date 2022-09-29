from django import forms
from django.db import connection

from .models import Pet


class PetAdoptForm(forms.Form):
    PET_BREED_CHOICES = []

    # Provide the available breeds from our database as choices
    if 'myapp_pet' in connection.introspection.table_names():
        for pet in Pet.objects.all():
            if (pet.breed, pet.breed) not in PET_BREED_CHOICES:
                PET_BREED_CHOICES.append((pet.breed, pet.breed))

    GENDER_CHOICES = (
        ("M", "Boy"),
        ("F", "Girl"),
        ("Both", "Don't care")
    )

    PET_SPECIES = (
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Both', 'Both make me happy')
    )

    pet = forms.ChoiceField(
        help_text="Do you want a Cat or a Dog?", widget=forms.RadioSelect, choices=PET_SPECIES)
    pet_gender = forms.ChoiceField(
        help_text="Do you want a boy or a girl?", widget=forms.RadioSelect, choices=GENDER_CHOICES)
    pet_age = forms.IntegerField(
        help_text="How old would you like your pet to be? (Leave empty if pet age is not an issue)",
        min_value=0,
        max_value=200,
        localize=False,
        required=False)
    pet_breed = forms.ChoiceField(
        help_text="Do you want a special breed of pet? (Leave default if breed doesn't matter to you)",
        required=False,
        choices=PET_BREED_CHOICES)
