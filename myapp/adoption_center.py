""" This module contains the adoption center methods.
"""
import random

# from .models import Pet


class AdoptionCenterFactory:
    """ Adoption Center Factory that provides the user
    with a desired animal from the Pool
    or a random animal that just got lucky.
    """

    def __init__(self, adoption_pool):
        self.adoption_pool = adoption_pool

    def finish_successful_adoption(self, animal):
        """ Finish the adoption by messaging the user and returning the adopted animal.
        Remove the animal from the pool once it has been adopted.

        :param animal: The animal to be adopted.
        :return tuple: Message about the adopted animal,
                        An animal object,
                        Modified adoption pool with adopted animal removed.
        """
        message = f"You adopted a {repr(animal)}."
        # Remove the animal from the pool once it has been adopted:
        self.adoption_pool = self.adoption_pool.exclude(pk=animal.pk)
        # TODO: Remove the pet record from the database. It throws an errors though
        # Pet.objects.get(pk=animal.pk).delete()
        return message, animal, self.adoption_pool

    @staticmethod
    def second_chance(pet_list):
        """ If the desired animal is not found,
        Message the user and return a list of additional animals to choose from.

        :param pet_list: A list of pets.
        :return tuple: Message about the unsuccessful adoption, A list of animal objects.
        """
        message = "Sorry, we don't have this pet in our shop!" \
                  " Would you consider adopting one of these cuties instead:"
        return message, None, pet_list

    def adopt_animal(self, breed, age, gender):
        """ Adopt any desired animal by breed, age and gender.

        :param breed: The desired breed of the animal.
        :param age: The desired age of the animal.
        :param gender: The desired gender of the animal.
        :return tuple: Message, pet object with the desired attributes, list of remaining pets OR
                tuple: Message, None, list of additional animals ordered by (breed > age > gender)
                      if the desired animal is not in the Pool.
        """
        if age is None and not breed and gender == 'Both':
            return self.get_lucky()

        if age is None and not breed:
            lucky_animal_list = [
                animal for animal in self.adoption_pool if animal.get_gender() == gender]

        elif not breed and gender == 'Both':
            lucky_animal_list = [animal for animal in self.adoption_pool if animal.get_age() == age]

        elif age is None and gender == 'Both':
            lucky_animal_list = [
                animal for animal in self.adoption_pool if animal.get_breed() == breed]

        elif age is None:
            lucky_animal_list = [
                animal for animal in self.adoption_pool
                if animal.get_breed() == breed
                and animal.get_gender() == gender]

        elif gender == 'Both':
            lucky_animal_list = [animal for animal in self.adoption_pool
                                 if animal.get_breed() == breed
                                 and animal.get_age() == age]

        elif not breed:
            lucky_animal_list = [animal for animal in self.adoption_pool
                                 if animal.get_age() == age
                                 and animal.get_gender() == gender]

        else:
            lucky_animal_list = [animal for animal in self.adoption_pool
                                 if animal.get_breed() == breed
                                 and animal.get_age() == age
                                 and animal.get_gender() == gender]

        # Return only one animal to not confuse the user with too many options:
        if len(lucky_animal_list) > 0:
            lucky_animal = lucky_animal_list[0]
            return self.finish_successful_adoption(lucky_animal)

        # If no such animal exists in the Pool,
        # propose an additional list of animals filtered and ordered by: breed > gender > age
        breed_list = [x for x in self.adoption_pool if x.breed == breed]
        gender_list = [x for x in self.adoption_pool if x.gender == gender]
        age_list = [x for x in self.adoption_pool if x.age == age]

        # Remove the duplicates from the final list:
        additional_possibilities = list(dict.fromkeys(breed_list + gender_list + age_list))

        return self.second_chance(additional_possibilities)

    def get_lucky(self):
        """ Get a random animal from the shop.
        :return tuple: Message about the adopted animal,
                       Animal object with random breed, age and gender.
        """
        lucky_animal = random.choice(self.adoption_pool)
        return self.finish_successful_adoption(lucky_animal)
