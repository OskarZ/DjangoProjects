from django.shortcuts import render
from django.http import HttpResponse



def ndex(request):
    return render(request, 'Startseite/umleitung.html', {})