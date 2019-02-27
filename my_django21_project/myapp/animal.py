""" This module contains the Animal, Dog and Cat classes.
"""

# A list of dog breeds that are available in the adoption center.
DOG_BREED = ["bulldog", "german shepherd", "labrador", "poodle", "goldren retriever", "chihuahua", "pug", "beagle",
             "dachshund", "yorkshire terrier", "bull terrier", "husky", "doberman", "rottweiler", "chow chow",
             "mastiff", "collie", "greyhound", "corgi", "dalmatian", "cocker spaniel", "unbred"]

# A list of cat breeds that are available in the adoption center.
CAT_BREED = ["russian blue", "persian", "british shorthair", "munchkin", "siamese", "sphynx", "savannah", "ragamuffin",
             "ragdoll", "maine coon", "unbred"]

# A tuple of possible animal genders
GENDER = ("M", "F")


class Animal:
    """ Define the Animal super class"""

    def __init__(self, name, breed, age, gender):
        """ Initialize an instance of the Animal class

        :param name: the name of the animal
        :param breed: the breed of the animal
        :param age: the age of the animal
        :param gender: the gender of the animal
        """
        self.name = str(name)
        self.breed = str(breed).lower()  # Convert breed to lowercase in order to match the breed lists
        self.age = int(age)
        self.gender = str(gender).capitalize()[0]  # Take only the first letter of the gender, capitalized

        assert self.gender in GENDER

    # This method is not used in the adoption process but it adds a nice touch and character to the animals.
    @staticmethod
    def eat(fav_food):
        """ What is the animal's favorite food?

        :param fav_food: my favorite food
        :return: I like to eat {fav_food}
        """
        return "I like to eat {}.".format(fav_food)


class Dog(Animal):
    """ Define the Dog child class. Inherits from Animal"""

    def __init__(self, name, breed, age, gender):
        """ Initialize attributes from the parent class Animal."""
        super().__init__(name, breed, age, gender)

        # Make sure that the breed of the dog is present in the list of possible dog breed values.
        assert self.breed in DOG_BREED

    def __repr__(self):
        """ Represent the object as Dog. Can be invoked with str(object)."""
        return "Dog"


class Cat(Animal):
    """ Define the Cat child class. Inherits from Animal"""

    def __init__(self, name, breed, age, gender):
        """ Initialize attributes from the parent class Animal."""
        super().__init__(name, breed, age, gender)

        # Make sure that the breed of the cat is present in the list of possible cat breed values.
        assert self.breed in CAT_BREED

    def __repr__(self):
        """ Represent the object as Cat. Can be invoked with str(object)."""
        return "Cat"
