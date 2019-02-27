from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from . import forms


def offer_list(request):
    pet_instance = render(request, 'index.html')
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = forms.PetAdoptForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            pet = form.cleaned_data['pet']
            pet_breed = form.cleaned_data['pet_breed']
            pet_gender = form.cleaned_data['pet_gender']
            pet_age = form.cleaned_data['pet_age']
            pet_instance.save()  # How does this work?
            # redirect to a new URL:
        return HttpResponseRedirect('/thanks/')
    # If this is a GET (or any other method) create the default form.
    else:
        form = forms.PetAdoptForm()

    return render(request, 'index.html', context={'form': form})
