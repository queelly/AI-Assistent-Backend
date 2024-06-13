from django.urls import path

from .views import ChadGPTAPIView

urlpatterns = [
    path('ask/', ChadGPTAPIView.as_view(), name='ask-chadgpt'),
]