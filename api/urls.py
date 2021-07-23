from django.urls import path
from api import views
urlpatterns = [
    path('face_recognition/',views.face_recognition),
    path('object_detection/',views.object_detection),
    path('depth_perception/',views.depth_perception),
    path('speech_to_text/',views.speech_to_text),
    path('text_detection/',views.text_detection),
    path('text_to_speech/',views.text_to_speech),
    path('voice_command/',views.voice_command),
    path('', views.testRoute),
]
