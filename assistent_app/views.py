from django.shortcuts import render, get_object_or_404
from rest_framework import generics, serializers
from rest_framework.response import Response

from assistent_app.models import AssistentThemeModel, ChatMessageModel
from assistent_app.services import FactoryState
from authentication import serializer


class AssistentSerializer(serializers.Serializer):
    theme = serializers.BooleanField(label="Показывать темы", required=False)

    theme_id = serializers.IntegerField(label="Выбранная тема", required=False)

    answer_id = serializers.IntegerField(label="Выбранный ответ", required=False)

    class Meta:
        fields = ['theme', 'theme_id', 'answer_id']


# Create your views here.
class AssistentTreeAPIView(generics.GenericAPIView):

    queryset = ChatMessageModel.objects.all()

    serializer_class = AssistentSerializer

    def post(self, request, *args, **kwargs):
        chat_option = FactoryState.create_chat_option(request)

        result = chat_option.result()

        return Response(data=result, status=200)
