from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import GptSerializer
import requests
#generic viewset
class ChadGPTAPIView(GenericAPIView):
    serializer_class = GptSerializer
    queryset = None
    def post(self, request, *args, **kwargs):
        serializer = GptSerializer(data=request.data)
        if serializer.is_valid():
            message = request.data.get("message","Как дела?")
            request_json = {
                "message": message,
                "api_key": "chad-c647e5d4d8fa4f0ca5457d4e62f965812ra1iudl",
            }
            response = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-3.5', json=request_json)
            if response.status_code == 200:
                resp_json = response.json()
                if resp_json['is_success']:
                    return Response({
                        'response': resp_json['response'],
                        'used_words_count': resp_json['used_words_count']
                    })
                else:
                    return Response({'error': resp_json['error_message']}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': f'Error! Code answer: {response.status_code}'}, status=response.status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)