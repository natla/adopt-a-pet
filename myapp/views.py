from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework import status

from . import forms
from .adoption_center import AdoptionCenterFactory
from .models import Pet
from .serializers import PetSerializer


def render_pet_adopt_form(request):
    """ Render a pet adoption form on the page

    :param request: HTTP request (GET or POST)
    :return: HTTP response (render the form on the page
    or a Thank You page on successful adoption)
    """

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = forms.PetAdoptForm(request.POST)

        if not form.is_valid():
            return HttpResponse(content=form.errors, status=status.HTTP_400_BAD_REQUEST)

        pet_species = form.cleaned_data['pet']
        pet_breed = form.cleaned_data['pet_breed']
        print('BREED', pet_breed)
        pet_gender = form.cleaned_data['pet_gender']
        print('GENDER', pet_gender)
        pet_age = form.cleaned_data['pet_age']
        print('AGE', pet_age)

        found_pets = Pet.objects.filter(species=pet_species) if pet_species != 'Both' else Pet.objects.all()
        adoption_pool = AdoptionCenterFactory(found_pets)
        message, result, pet_list = adoption_pool.adopt_animal(breed=pet_breed, age=pet_age, gender=pet_gender)
        if result is None:
            return render(request, 'pet-not-found.html', {'message': message, 'pet_list': pet_list})

        return HttpResponseRedirect(reverse_lazy('myapp:pet_adopted', kwargs={'pk': result.id}))

    # If this is a GET method render the default form
    form = forms.PetAdoptForm()

    return render(request, 'form.html', {'form': form})


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_pet(request, pk: int):
    """ Get, delete or update a single pet record

    :param request: HTTP request (GET, DELETE or PUT)
    :param pk: Pet primary key
    :return: HTTP response
    """
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single Pet
    if request.method == 'GET':
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    # update details of a single Pet
    if request.method == 'PUT':
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single Pet
    if request.method == 'DELETE':
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_pets(request):
    """ Get all pets in the database or insert a new pet record

    Example how to insert a valid new record:
        {
        "species": "Dog",
        "name": "Muffin",
        "breed": "Pomeranian",
        "gender": "M",
        "age": 4
    }
    """
    # get all puppies
    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    # insert a new record for a Pet
    if request.method == 'POST':
        data = {
            'species': request.data.get('species'),
            'name': request.data.get('name'),
            'breed': request.data.get('breed'),
            'gender': request.data.get('gender'),
            'age': int(request.data.get('age'))
        }
        serializer = PetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def pet_detail_view(request, pk: int):
    """
    Render the detailed page view of a single pet

    :param request: HTTP request (GET or POST)
    :param pk: Pet primary key
    :return: HTTP response
    """
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'detail.html', {'pet': pet})


def pet_gallery_view(request):
    """
    Render the gallery view of all pets for adoption in the database

    :param request: HTTP request (GET or POST)
    :return: HTTP response
    """
    pets = Pet.objects.all()
    return render(request, 'pets.html', {'pets': pets})


def pet_adopted(request, pk: int):
    """
    Render the thank you page of an adopted animal

    :param request: HTTP request (GET or POST)
    :param pk: Id of the animal that gets adopted
    :return: HTTP response
    """
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'thanks.html', {'pet': pet})
