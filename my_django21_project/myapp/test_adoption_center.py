""" This module provides tests for the Dog class and the adoption center methods
"""

import unittest
from adoption_center import AdoptionCenterFactory
from animal import Animal, Dog, Cat


class TestAdoptionService(unittest.TestCase):
    def setUp(self):
        """ Create animals for testing purposes.
        """
        self.sharo = Dog('Sharo', 'unbred', 5, "male")
        self.assertIsInstance(self.sharo, Dog)
        self.lucy = Dog('Lucy', 'collie', 3, "Female")
        self.assertNotIsInstance(self.lucy, Cat)
        self.daisy = Dog('Daisy', 'labrador', 2, "fem")
        self.rocco = Dog('Rocco', 'German Shepherd', 1, "M")
        self.duke = Dog('Duke', 'Doberman', 4, "Male")
        self.max_ = Dog('Max', 'greyhound', 7, "M")  # Using a trailing underscore because max is a keyword in Python

        self.maya = Cat('Maya', 'Sphynx', 5, "F")
        self.assertIsInstance(self.maya, Cat)
        self.ruh = Cat('Ruh', 'unbred', 3, "male")
        self.assertNotIsInstance(self.ruh, Dog)
        self.tiger = Cat('Tiger', 'SAVANNAH', 4, "M")
        self.assertIsInstance(self.tiger, Animal)


        # Create a non-animal object
        self.non_animal_object = (5, "F")
        self.assertIsNot(self.non_animal_object, Animal)

        # Create a Pool with dogs for adoption   # TODO - take the animals from a database instead
        self.dog_pool = [self.sharo, self.lucy, self.daisy, self.rocco, self.duke, self.max_]
        # Create a Pool with cats for adoption
        self.cat_pool = [self.maya, self.ruh, self.tiger]

    def test_age(self):
        """ Test the age of the animal instances
        """
        self.assertEqual(self.sharo.age, 5)
        self.assertNotEqual(self.daisy.age, 512)

    def test_breed(self):
        """ Test the breed of the animal instances
        """
        self.assertEqual(self.lucy.breed, 'collie')
        # Akita breed is not in the list of possible breeds:
        with self.assertRaises(AssertionError):
            Dog('Mollie', 'Akita', 6, 'Male')

    def test_gender(self):
        """ Test the gender of the animal instances
        """
        self.assertEqual(self.rocco.gender, 'M')
        with self.assertRaises(AssertionError):
            Dog('Bobby', 'chow chow', 6, 'Unknown_gender')

    def test_eat_method(self):
        """ Test the eat method of the animal instances
        """
        self.assertEqual("I like to eat bones.", self.sharo.eat("bones"))
        self.assertEqual("I like to eat fish.", self.ruh.eat("fish"))
        self.assertEqual("I like to eat chicken soup.", self.tiger.eat("chicken soup"))

    def test_adoption_methods(self):
        """ Test the adoption methods of the Adoption Center Factory
        """
        dog_adoption_center = AdoptionCenterFactory(self.dog_pool)
        cat_adoption_center = AdoptionCenterFactory(self.cat_pool)

        # Adopt a dog that exists in the Pool
        message, result = dog_adoption_center.adopt_animal("doberman", 4, "M")
        self.assertIsInstance(result, Dog)
        # Assert that the adopted dog has been removed from the Dog pool
        self.assertNotIn(result, self.dog_pool)
        # Assert that the user received a proper message
        self.assertEqual("You adopted a {} named {} that is {} years old and a {}."
                         .format(str(result), result.name,
                                 result.age,
                                 'boy' if result.gender == 'M' else 'girl'),
                         message)

        # Try to adopt a dog that doesn't exist in the Pool
        message, result_list = dog_adoption_center.adopt_animal("labrador", 3, "F")
        # Assert that the proper message has been returned
        self.assertIn("Sorry, we currently don't have such an animal in our shop!"
                      " Would you consider adopting an animal from this list instead: ", message)

        # Adopt a random cat from the Pool
        message, result = cat_adoption_center.get_lucky()
        # Assert that the lucky cat has been removed from the Dog pool
        self.assertNotIn(result, self.cat_pool)
        # Assert that the user received a proper message
        self.assertEqual("You adopted a {} named {} that is {} years old and a {}."
                         .format(str(result), result.name,
                                 result.age,
                                 'boy' if result.gender == 'M' else 'girl'),
                         message)


if __name__ == '__main__':
    unittest.main()
