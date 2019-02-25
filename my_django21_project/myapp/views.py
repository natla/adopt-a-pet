from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.utils import timezone
from .models import Post
from . import forms


def index(request):
    return render(request, 'index.html')


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


def post_detail_view(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'blog/post/detail.html', {'post': post})


def post_list_view(request):
    list_objects = Post.published.all()
    paginator = Paginator(list_objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def sim_bios(request):
    return render(request, 'blog/bios.html')


def blog_contact(request):
    return render(request, 'blog/contact.html')
