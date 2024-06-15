from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import GptSerializer, GptSerializerFilter
import requests


# generic viewset
class ChadGPTAPIView(GenericAPIView):
    serializer_class = GptSerializer
    queryset = None

    def post(self, request, *args, **kwargs):
        serializer = GptSerializer(data=request.data)
        if serializer.is_valid():
            message = request.data.get("message", "Как дела?")
            request_json = {
                "message": message,
                "api_key": "chad-c647e5d4d8fa4f0ca5457d4e62f965812ra1iudl",
                "history": [
                    {"role": "system",
                     "content": "Ты - полезный ассистент в области инвестиций. Ты знаешь только все, что касается инвестиций! Если человек задает вопрос не по делу, отвечай <<Это не моя компетенция>>."},
                ]
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


class ChadGPTFiltreCategoryView(GenericAPIView):
    serializer_class = GptSerializerFilter
    queryset = None

    def post(self, request, *args, **kwargs):
        serializer = GptSerializerFilter(data=request.data)
        if serializer.is_valid():
            message = request.data.get("message", "Как дела?")
            category = request.data.get("category", "Технопарк")
            if (category == "Технопарк" or category == "ОЭЗ"):
                request_json = {
                    "message": message,
                    "api_key": "chad-c647e5d4d8fa4f0ca5457d4e62f965812ra1iudl",
                    "history": [
                        {"role": "system",
                         "content": "Ты - полезный ассистент в области инвестиций. "
                                    "Если человек задает вопрос не по делу, отвечай <<Это не моя компетенция>>."
                                    " Тебе дан список категорий  и дано сообщение пользователя. "
                                    "Если человек имеет ввиду категорию которая есть в списке категорий,"
                                    " то ответь  этой категорией и через двоеточие напиши значение, "
                                    "которое относится к этой категории ,если в сообщении пользователя категорий несколько, "
                                    "то напиши несколько категорий  о которых вел речь пользователь и через двоеточие их значения."
                                    "Если подразумевает, что значение категории о которой идет речь равна нулю или отсутсвует, то через двоеточие напиши <<0>>"
                                    "Если категория подразумевает численное значение или дату, то всегда через двоеточие пиши число."
                                    "Если ни к одной категории не относится,  "
                                    "то напиши <<Извините я не понимаю о чем вы>>. "
                                    " Сам список категорий: Наименование объекта, Муниципальное образование, Количество резидентов ,"
                                    "Год формирования объекта ,Срок действия объекта,Общая площадь ,Список отраслей , "
                                    "Налог на прибыль, Налог на имущество ,Земельный налог, Транспортный налог,Страховые взносы "
                                    ",Минимальный объем инвестиций. Выдай как в примере.  Пример: Налог : 0, Наименование: Технополис"},

                    ]
                }
            if (category == "РМП"):
                request_json = {
                    "message": message,
                    "api_key": "chad-c647e5d4d8fa4f0ca5457d4e62f965812ra1iudl",
                    "history": [
                        {"role": "system",
                         "content": "Ты - полезный ассистент в области инвестиций. "
                                    "Если человек задает вопрос не по делу, отвечай <<Это не моя компетенция>>."
                                    " Тебе дан список категорий  и дано сообщение пользователя. "
                                    "Если человек имеет ввиду категорию которая есть в списке категорий,"
                                    " то ответь  этой категорией и через двоеточие напиши значение, "
                                    "которое относится к этой категории ,если в сообщении пользователя категорий несколько, "
                                    "то напиши несколько категорий  о которых вел речь пользователь и через двоеточие их значения."
                                    "Если подразумевает, что значение категории, о которой идет речь равна нулю или отсутсвует, то через двоеточие напиши <<0>>"
                                    "Если ни к одной категории не относится,  "
                                    "то напиши <<Извините я не понимаю о чем вы>>. "
                                    "Сам список категорий: Список отраслей,  Налог на прибыль ,Налог на имущество ,"
                                    "Земельный налог, Транспортный налог ,Страховые взносы , Минимальный объем инвестиций.  "
                                    "Выдай как в примере.  Пример: Налог : 0, Наименование: Технополис"},
                    ]
                }
            if (category == "Помещения и Сооружения"):
                request_json = {
                    "message": message,
                    "api_key": "chad-c647e5d4d8fa4f0ca5457d4e62f965812ra1iudl",
                    "history": [
                        {"role": "system",
                         "content": "Ты - полезный ассистент в области инвестиций. "
                                    "Если человек задает вопрос не по делу, отвечай <<Это не моя компетенция>>."
                                    " Тебе дан список категорий  и дано сообщение пользователя. "
                                    "Если человек имеет ввиду категорию которая есть в списке категорий,"
                                    " то ответь  этой категорией и через двоеточие напиши значение, "
                                    "которое относится к этой категории ,если в сообщении пользователя категорий несколько, "
                                    "то напиши несколько категорий  о которых вел речь пользователь и через двоеточие их значения."
                                    "Если подразумевает, что значение категории, о которой идет речь равна нулю или отсутсвует, то через двоеточие напиши <<0>>"
                                    "Если ни к одной категории не относится,  "
                                    "то напиши <<Извините я не понимаю о чем вы>>. "
                                    "Сам список категорий: Муниципальное образование, Тип площадки, Форма собственности объекта,"
                                    "Стоимость объекта ,Стоимость руб./год за га, Стоимость, руб./год за га,min и max сроки аренды ,"
                                    "Свободная площадь ЗУ га, Варианты разрешенного использования, Свободная площадь, "
                                    "Водоснабжение Наличие,Водоотведение Наличие,Газоснабжение Наличие,Электроснабжение Наличие,"
                                    "Теплоснабжение Наличие,Вывоз ТКО Наличие,Наличие подъездных путей,Наличие ж/д,Наличие парковки грузового транспорта "
                                    " Выдай как в примере.  Пример: Налог : 0, Наименование: Технополис"},
                    ]
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
