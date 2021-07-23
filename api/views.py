from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def usersApi(request):
    return HttpResponse("Ok! Working ")

