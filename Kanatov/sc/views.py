
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, View
from .models import *
from django.contrib.contenttypes.models import ContentType
# Create your views here.


class Home(ListView):
    model = Student
    context_object_name = 'product'
    template_name = 'sc/base.html'
    extra_context = {'student': Student.objects.all()}
    slug_url_kwarg = 'slug'