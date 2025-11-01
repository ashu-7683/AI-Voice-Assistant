from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('api/response/', views.ai_response, name='ai_response'),
]
