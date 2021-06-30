from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView 
from django.views import View

class Home(View):
    def get(self, request):
        return HttpResponse('HOME PAGE!')
