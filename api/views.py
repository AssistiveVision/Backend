from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

def face_recognition(request):
    return HttpResponse("Ok face_recognition! Working ")

def object_detection(request):
    return HttpResponse("Ok object_detection! Working ")

def depth_perception(request):
    return HttpResponse("Ok depth_perception! Working ")

def speech_to_text(request):
    return HttpResponse("Ok speech_to_text! Working ")

def text_detection(request):
    return HttpResponse("Ok text_detection! Working ")

def text_to_speech(request):
    return HttpResponse("Ok text_to_speech! Working ")

def voice_command(request):
    return HttpResponse("Ok voice_command! Working ")

def testRoute(request):
    return HttpResponse("Ok! Working ")

