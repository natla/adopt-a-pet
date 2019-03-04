from django import forms


class PetAdoptForm(forms.Form):
    # A list of dog breeds for testing purposes
    # TODO: Take the list of dog breeds that are available in the adoption center from the database.
    DOG_BREED = ["bulldog", "german shepherd", "labrador", "poodle",
                 "goldren retriever", "chihuahua", "pug", "beagle",
                 "dachshund", "yorkshire terrier", "bull terrier",
                 "husky", "doberman", "rottweiler", "chow chow",
                 "mastiff", "collie", "greyhound", "corgi",
                 "dalmatian", "cocker spaniel", "unbred"]

    # A list of cat breeds for testing purposes
    # TODO: Take the list of cat breeds that are available in the adoption center from the database.
    CAT_BREED = ["russian blue", "persian", "british shorthair",
                 "munchkin", "siamese", "sphynx", "savannah",
                 "ragamuffin", "ragdoll", "maine coon", "unbred"]

    # A tuple of binary animal genders
    GENDER = (
        ("M", "Boy"),
        ("F", "Girl"),
        ("Other", "Don't care")
    )
    SPECIES = (
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Both', 'Both make me happy')
    )

    pet = forms.ChoiceField(help_text="Do you want a Cat or a Dog?", widget=forms.RadioSelect,
                            choices=SPECIES)
    pet_gender = forms.ChoiceField(help_text="Do you want a boy or a girl?",
                                   widget=forms.RadioSelect, choices=GENDER)
    pet_age = forms.IntegerField(
        help_text="How old would you like your pet to be? (Leave empty if pet age is not an issue)",
        min_value=0, max_value=200, localize=False, required=False)
    pet_breed = forms.ChoiceField(
        help_text="Do you want a special breed of pet? (Leave default if breed doesn't matter to you)",
        widget=forms.TextInput, required=False, initial="unbred")

    # def clean_pet_gender(self):
    #     data = self.cleaned_data['pet_gender']
    #
    #     # Remember to always return the cleaned data.
    #     return data
