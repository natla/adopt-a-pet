from django.db import models
from django.urls import reverse
import re

class Pet(models.Model):
    """
    Pet Model
    Defines the attributes of a pet
    """
    GENDER = (
        ("M", "Boy"),
        ("F", "Girl"),
    )
    species = models.CharField(max_length=30, default="Dog")
    name = models.CharField(max_length=50, unique=True)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField()

    def get_name(self):
        """ Get the name of the pet. """
        return self.name

    def get_breed(self):
        """ Get the breed of the pet. """
        return self.breed

    def get_age(self):
        """ Get the age of the pet. """
        return self.age

    def get_gender(self):
        """ Get the gender of the pet: M, F or Other. """
        return self.gender

    # This method is not being used yet in the adoption process but it adds pet personality.
    @staticmethod
    def eat(fav_food):
        """ What is the pet's favorite food?

        :param fav_food: my favorite food
        :return: I like to eat {fav_food}
        """
        return "I like to eat {}.".format(fav_food)

    def __repr__(self):
        """ User-friendly representation of the pet object. Will be invoked by repr(object)."""
        if self.get_gender() is not 'Other':
            return "{} named {} that is {} and a {}" \
                .format(self.breed.capitalize(),
                        self.name,
                        str(self.age) + " years old",
                        'boy' if self.get_gender() == 'M' else 'girl')
        else:
            return "{} named {} that is {}" \
                .format(self.breed.capitalize(),
                        self.name,
                        str(self.age) + " years old")

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('myapp:pet_detail_view', kwargs={'pk': self.pk})
