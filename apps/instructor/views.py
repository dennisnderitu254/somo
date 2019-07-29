from django.shortcuts import render
from django.views.generic import View, TemplateView


class Index(View):
    template_name = 'index.html'

class About(View):
    template_name = 'about.html'

class Contacts(View):
    template_name = 'contacts.html'

    

    












