from django import forms
from .animal import DOG_BREED, CAT_BREED, GENDER


class PetAdoptForm(forms.Form):
    pet = forms.ChoiceField(help_text="Do you want a Cat or a Dog?", widget=forms.RadioSelect, choices=['Cat', 'Dog', 'Both make me happy'], required=False)
    pet_gender = forms.ChoiceField(help_text="Do you want a boy or a girl? (Don't care is an option)", widget=forms.RadioSelect, choices=GENDER,
                                   required=False)
    pet_age = forms.IntegerField(
        help_text="How old would you like your pet to be? (Leave empty if pet age is not an issue)",
        min_value=0, max_value=200, localize=False, required=False)
    pet_breed = forms.ChoiceField(help_text="Do you want a special breed of pet? (Leave empty if breed doesn't matter to you)", choices=DOG_BREED + CAT_BREED,
                                  widget=forms.TextInput, required=False, initial="unbred")

    # def clean_pet_gender(self):
    #     data = self.cleaned_data['pet_gender']
    #
    #     # Remember to always return the cleaned data.
    #     return data
