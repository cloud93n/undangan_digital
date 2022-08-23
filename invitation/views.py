from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'