from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('start/index-1.html')
    return render(request, 'start/index-1.html')

