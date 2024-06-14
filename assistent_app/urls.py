from django.urls import path

from .views import AssistentTreeAPIView, FilterSuggestion

urlpatterns = [
    path('filter', FilterSuggestion.as_view(),),
    path('', AssistentTreeAPIView.as_view()),
]