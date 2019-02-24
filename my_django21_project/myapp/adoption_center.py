""" This module contains the adoption center methods.
"""

import random


class AdoptionCenterFactory:
    """ Adoption Center Factory that provides the adopter with a desired animal from the Pool
    or a random animal that just got lucky.
    """

    def __init__(self, adoption_pool):
        self.adoption_pool = adoption_pool

    def adopt_animal(self, breed, age, gender):
        """ Adopt any desired animal by breed, age and gender.

        :param breed: The desired breed of the animal.
        :param age: The desired age of the animal.
        :param gender: The desired gender of the animal.
        :return: A tuple of a suitable message and an animal object with the desired attributes OR
                 A tuple of a suitable message and a list of additional animals if the desired animal is not in the Pool
                 The additional list of animals is ordered by: breed + age/ breed + gender/ age + gender
                 based on the relative importance of these attributes (breed > age > gender)
        """
        for animal in self.adoption_pool:
            if animal.breed == breed and animal.age == age and animal.gender == gender:
                message = "You adopted a {} named {} that is {} years old and a {}.".format(str(animal), animal.name,
                                                               animal.age, 'boy' if animal.gender == 'M' else 'girl')
                # Remove the animal from the pool once it has been adopted
                self.adoption_pool.remove(animal)
                return message, animal

        # If no such animal exists in the Pool
        # Propose an additional list of animals ordered by: breed + age/ breed + gender/ age + gender
        additional_possibilities = []
        for animal in self.adoption_pool:
            if animal.breed == breed and animal.age == age:
                additional_possibilities.append((animal.name, animal.breed, str(animal.age) + " years old",
                                                 'boy' if animal.gender == 'M' else 'girl'))
            elif animal.breed == breed and animal.gender == gender:
                additional_possibilities.append((animal.name, animal.breed, str(animal.age) + " years old",
                                                 'boy' if animal.gender == 'M' else 'girl'))
            elif animal.age == age and animal.gender == gender:
                additional_possibilities.append((animal.name, animal.breed, str(animal.age) + " years old",
                                                 'boy' if animal.gender == 'M' else 'girl'))
        message = "Sorry, we currently don't have such an animal in our shop!" \
                  " Would you consider adopting an animal from this list instead: {}.".format(additional_possibilities)
        return message, additional_possibilities

    def get_lucky(self):
        """ Get a random animal from the shop.
        :return: An animal object with random breed, age and gender.
        """
        lucky_animal = random.choice(self.adoption_pool)  # or random.randint(the index of the animal from the pool)
        message = "You adopted a {} named {} that is {} years old and a {}.".format(str(lucky_animal), lucky_animal.name,
                                              lucky_animal.age, 'boy' if lucky_animal.gender == 'M' else 'girl')
        # Remove the animal from the pool once it has been adopted
        self.adoption_pool.remove(lucky_animal)
        return message, lucky_animal

