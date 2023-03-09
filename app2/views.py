from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pooji(request):
    return HttpResponse('she is my sister')