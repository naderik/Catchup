from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render())


def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
