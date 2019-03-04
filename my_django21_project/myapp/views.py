from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import forms
from .models import Pet
from .serializers import PetSerializer


def render_pet_adopt_form(request):
    """ Render a pet adoption form on the page

    :param request: HTTP request (GET or POST)
    :return: HTTP response (render the form on the page
    """
    pet_instance = render(request, 'form.html')
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = forms.PetAdoptForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            pet_species = form.cleaned_data['pet']
            pet_breed = form.cleaned_data['pet_breed']
            pet_gender = form.cleaned_data['pet_gender']
            pet_age = form.cleaned_data['pet_age']
            pet_instance.save()
            # redirect to a new URL:
            # TODO: Implement the logic and create the redirect page
        return HttpResponseRedirect('/form/thanks/')
    # If this is a GET (or any other method) create the default form.
    else:
        form = forms.PetAdoptForm()

    return render(request, 'form.html', {'form': form})


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_pet(request, pk):
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
    elif request.method == 'PUT':
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single Pet
    elif request.method == 'DELETE':
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
    elif request.method == 'POST':
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

def pet_detail_view(request, pk):
    """ Render the detailed page view of a single pet

    :param request: HTTP request (GET or POST)
    :param pk: Pet primary key
    :return: HTTP response
    """
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'detail.html', {'pet': pet})

def pet_gallery_view(request):
    """ Render the gallery view of all pets for adoption in the database

    :param request: HTTP request (GET or POST)
    :return: HTTP response
    """
    pets = Pet.objects.all()
    return render(request, 'pets.html', {'pets': pets})

def pet_adopted(request, pk):
    """ Render the thank you page of an adopted animal

    :param request: HTTP request (GET or POST)
    :return: HTTP response
    """
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'thanks.html', {'pet': pet})
