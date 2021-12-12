import re
from django.shortcuts import render
import io 
import PIL.Image as Image
from services.depth_perception import depth_perception_service 
from django.http import JsonResponse

from django.http import HttpResponse
# Create your views here

def face_recognition(request):
    return HttpResponse("Ok face_recognition! Working ")

def object_detection(request):
    return HttpResponse("Ok object_detection! Working ")

#import matplotlib.pyplot as plt
import numpy as np  
import base64
def depth_perception(request):
    if request.method=="POST":
        #print(request.POST)
        x,y,w,h=request.POST['x'],request.POST['y'],request.POST['w'],request.POST['h']
        image_byte_data=request.FILES['image']    
        image = Image.open(image_byte_data)
        image = image.resize((640, 480), Image.ANTIALIAS)
        image = np.clip(np.asarray(image, dtype=float) / 255, 0, 1)
        #plt.imshow(image)
        #plt.show()
        output=depth_perception_service.predict_api(image)
        
        # this portions shares image in json 
        print(output)
        encoded_string = str(base64.b64encode(output.tobytes()))
        json_output={
            'output':encoded_string
        }
        return JsonResponse(json_output)
        # json work end 
    return render(request,template_name="api/form.html")

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