from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from assistent_app.models import AssistentThemeModel, ChatMessageModel
from assistent_app.services import FactoryState


# Create your views here.
class AssistentTreeAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        chat_option = FactoryState.create_chat_option(request)

        result = chat_option.result()

        return Response(data=result,status=200)






