from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
import logging
from .decorators import user_not_authenticated, base_view, BaseView
from .forms import *
from .models import Product, AboutMe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages

from .utils import grecaptcha_verify

logger = logging.getLogger(__name__)

# Navigation bar content
menu = [{'title': "Catalog", 'url_name': 'catalog'},
        {'title': "Service", 'url_name': 'service'},
        {'title': "Product", 'url_name': 'product'},
        {'title': "Contact", 'url_name': 'contact'},
        ]

# Mixin
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

# Function to return main page
def index(request):
    posts = Product.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'test/index.html', context=context)


# Function to return home page
def home(request):
    return render(request, 'test/index.html', {'title': 'Bang.in'})

# Function to return Service page
def service(request):
    return render(request, 'test/../articles/templates/service.html', {'title': 'Service'})

# Function to return Product page
def product(request):
    posts = Product.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Catalog',
    }
    return render(request, 'test/catalog.html', context=context)

# Function to return Info About us page
def about_us(request):
    posts = AboutMe.objects.all()
    odd_posts = posts[0::2]
    even_posts = posts[1::2]
    context = {
        'posts': posts,
        'title': 'About Us',
        'odd_posts': odd_posts,
        'even_posts': even_posts,
    }
    return render(request, 'test/about_us.html', context=context)

# Function to show the post
@login_required()
def show_post(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'test/post.html', context=context)

# Function to return settings page
@login_required()
def setting(request):
    return render(request, 'test/setting.html', {'title': 'Settings'})

# Login

# Feedback function
@base_view
@login_required()
def contactFormView(request):
    try:
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.save()
                print(form.cleaned_data)
                return redirect('home')

            else:
                for error in list(form.errors.values()):
                    messages.error(request, error, f'Something is wrong!')
                    logger.exception('Something is wrong!')

        else:
            form = FeedbackForm()
    except Exception as e:
        messages.error(request, f"An error occurred: {e}", 'Something is wrong!')
        logger.exception('Something is wrong!')
    return render(
        request=request,
        template_name='test/contact.html',
        context={"form": form}
    )
