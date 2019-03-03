from rest_framework.test import APITestCase
from ..models import Pet
from ..adoption_center import AdoptionCenterFactory


# Create your tests here.
class TestAdoptionService(APITestCase):
    def setUp(self):
        """ Create animals for testing purposes.
        """
        self.sharo = Pet.objects.create(species="Dog", name='Sharo', breed='unbred', age=5, gender="male")
        self.lucy = Pet.objects.create(species="Dog", name='Lucy', breed='collie', age=3, gender="Female")
        self.daisy = Pet.objects.create(species="Dog", name='Daisy', breed='labrador', age=2, gender="fem")
        self.rocco = Pet.objects.create(species="Dog", name='Rocco', breed='German Shepherd', age=1, gender="M")
        self.duke = Pet.objects.create(species="Dog", name='Duke', breed='Doberman', age=4, gender="Male")
        self.mike = Pet.objects.create(species="Dog", name='Mike', breed='Doberman', age=4, gender="Male")
        self.max_ = Pet.objects.create(species="Dog", name='Max', breed='greyhound', age=7, gender="M")
        self.bobby = Pet.objects.create(species="Dog", name='Bobby', breed='chow chow', age=6, gender='Unknown_gender')

        self.maya = Pet.objects.create(species="Cat", name='Maya', breed='Sphynx', age=5, gender="F")
        self.ruh = Pet.objects.create(species="Cat", name='Ruh', breed='unbred', age=3, gender="male")
        self.tiger = Pet.objects.create(species="Cat", name='Tiger', breed='SAVANNAH', age=4, gender="M")

        # Create a non-animal object
        self.non_animal_object = (5, "F")

        # Create a Pool with dogs for adoption
        self.dog_pool = Pet.objects.filter(species="Dog")
        # Create a Pool with cats for adoption
        self.cat_pool = Pet.objects.filter(species="Cat")

    def test_class_instances(self):
        """Test the class of the set-up animal instances
        """
        self.assertIsInstance(self.sharo, Pet)
        self.assertIsInstance(self.maya, Pet)
        self.assertIsNot(self.non_animal_object, Pet)

    def test_animal_age(self):
        """ Test the age of the animal instances
        """
        self.assertEqual(self.sharo.get_age(), 5)
        self.assertNotEqual(self.daisy.get_age(), 512)

    def test_animal_breed(self):
        """ Test the breed of the animal instances
        """
        self.assertEqual(self.lucy.get_breed(), 'collie')

    def test_animal_gender(self):
        """ Test the gender of the animal instances
        """
        self.assertEqual(self.rocco.get_gender(), 'M')
        self.assertEqual(self.bobby.get_gender(), 'Other')

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
        message, result, self.dog_pool = dog_adoption_center.adopt_animal("doberman", 4, "M")
        self.assertIsInstance(result, Pet)
        # Assert that the adopted dog has been removed from the Dog pool:
        self.assertNotIn(result, self.dog_pool)
        # Assert that the user received a proper message and only Duke is returned:
        self.assertEqual("You adopted a Doberman named Duke that is 4 years old and a boy.", message)

        # Try to adopt a dog that doesn't exist in the Pool
        message, result_list = dog_adoption_center.adopt_animal("labrador", 3, "F")
        # Assert that the proper message has been returned
        self.assertIn("Sorry, we don't have this pet in our shop!"
                      " Would you consider adopting one of these cuties instead: ", message)
        self.assertIn("Daisy", repr(result_list[0]))  # Daisy has same breed + gender
        self.assertIn("Lucy", repr(result_list[1]))  # Lucy has same gender + age

        # Adopt a random cat from the Pool
        message, result, self.cat_pool = cat_adoption_center.get_lucky()
        self.assertIsInstance(result, Pet)
        # Assert that the lucky cat has been removed from the Cat pool
        #self.assertNotIn(result, self.cat_pool)
        # Assert that the user received a proper message
        self.assertEqual("You adopted a {}." .format(repr(result)), message)
