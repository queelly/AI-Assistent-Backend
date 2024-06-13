from django.urls import path

from .views import AssistentTreeAPIView

urlpatterns = [
    path('', AssistentTreeAPIView.as_view())
]