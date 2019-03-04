import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import Client
from django.urls import reverse
from ..models import Pet
from ..serializers import PetSerializer

# initialize the APIClient app
client = Client()


class GetPuppiesTest(APITestCase):
    """ Test module for GET all pets API """

    def setUp(self):
        self.lucy = Pet.objects.create(species="Dog", name='Lucy', breed='collie', age=3, gender="F")

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('myapp:get_post_pets'))
        # get data from db
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_Pet(self):
        response = client.get(
            reverse('myapp:get_delete_update_pet', kwargs={'pk': self.lucy.pk}))
        pet = Pet.objects.get(pk=self.lucy.pk)
        serializer = PetSerializer(pet)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_Pet(self):
        response = client.get(
            reverse('myapp:get_delete_update_pet', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPetTest(APITestCase):
    """ Test module for inserting a new Pet """

    def setUp(self):
        self.valid_payload = {
            "species": "Dog",
            "name": "Daisy",
            "breed": "Labrador",
            "gender": "F",
            "age": 2
        }
        self.invalid_payload = {
            "species": "Dog",
            "name": "",
            "breed": "Labrador",
            "gender": "fem",
            "age": 2
        }

    def test_create_valid_pet(self):
        response = client.post(
            reverse('myapp:get_post_pets'),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_pet(self):
        response = client.post(
            reverse('myapp:get_post_pets'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePetTest(APITestCase):
    """ Test module for updating an existing Pet record """

    def setUp(self):
        self.duke = Pet.objects.create(species="Dog", name='Duke', breed='Doberman', age=4, gender="M")
        self.maya = Pet.objects.create(species="Cat", name='Maya', breed='Sphynx', age=5, gender="F")
        self.valid_payload = {
            "species": "Dog",
            "name": "Duke",
            "breed": "Labrador",
            "gender": "M",
            "age": 4
        }
        self.invalid_payload = {
            "species": "Cat",
            "name": "Maya",
            "breed": "",
            "gender": "F",
            "age": 5
        }

    def test_valid_update_pet(self):
        response = client.put(
            reverse('myapp:get_delete_update_pet', kwargs={'pk': self.duke.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_pet(self):
        response = client.put(
            reverse('myapp:get_delete_update_pet', kwargs={'pk': self.maya.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePetTest(APITestCase):
    """ Test module for deleting an existing Pet record """

    def setUp(self):
        self.duke = Pet.objects.create(species="Dog", name='Duke', breed='Doberman', age=4, gender="Male")

    def test_valid_delete_pet(self):
        response = client.delete(
            reverse('myapp:get_delete_update_pet', kwargs={'pk': self.duke.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_pet(self):
        response = client.delete(
            reverse('myapp:get_delete_update_pet', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
