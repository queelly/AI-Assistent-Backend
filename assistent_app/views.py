from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from assistent_app.models import AssistentThemeModel, ChatMessageModel


# Create your views here.
class AssistentTreeAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        theme = request.GET.get("theme", False)

        # Показываем список тем
        if theme:
            return self.get_theme_list()

        theme_id = request.GET.get('theme_id', None)

        # Тема выбрана
        if theme_id:
            return self.get_theme_questions(theme_id)

        answer_id = request.GET.get('answer_id', None)

        # Обрабатываем ответ пользователя
        if answer_id:
            return self.get_message_answer(answer_id)

        return_parent_id = request.GET.get('return_parent_id', None)

        # Возвращаемся назад к предыдущиму вопросу
        if return_parent_id:
            return self.return_back_message(return_parent_id)


        return Response(status=400)

    def get_theme_list(self):

        response = []

        themes = AssistentThemeModel.objects.filter(is_active=True)

        for theme in themes:
            response.append({"id": theme.id, "text": theme.title})

        return Response(data=response, status=200)

    def get_theme_questions(self, theme_id):
        theme_parent = get_object_or_404(AssistentThemeModel, id=theme_id)

        # Получаем все дочерние узлы с is_assistent=False (вопросы)
        questions = ChatMessageModel.objects.filter(theme=theme_parent, depth=1)

        response_data = []
        for question in questions:
            response_data.append({
                "answer_id": question.id,
                "answer_text": question.message,
            })

        return Response(data=response_data, status=200)

    def get_message_answer(self, answer_id):
        answer_node = get_object_or_404(AssistentThemeModel, id=answer_id)

        question = answer_node.get_parent()

        answer_node = answer_node.get_first_child()

        # Получаем дочерние узлы вопроса (возможные ответы)
        answers = []
        for child_answer in answer_node.get_children():
            answers.append({"answer_text": child_answer.message, "id": child_answer.id})

        # Определяем parent_answer_id (если есть родитель у вопроса)
        parent_answer_id = None

        if question:
            if question.get_depth() > 1:  # Проверяем, есть ли родитель у вопроса
                parent_answer_id = question.get_parent().id

        return Response(data={
            # "question": question.message,A
            "bot_answer": answer_node.message,
            "answers": answers,
            "parent_answer_id": parent_answer_id
        })

    def return_back_message(self, return_parent_id):
        # Получаем узел с заданным return_parent_id (ответ)
        child_answer = get_object_or_404(AssistentThemeModel, id=return_parent_id)

        # Получаем родительский узел (вопрос)
        question = child_answer.get_parent()

        # Получаем дочерние узлы вопроса (возможные ответы)
        answers = []
        for answer in question.get_children():
            answers.append({"text": answer.message, "id": answer.id})

        # Определяем parent_answer_id (если есть родитель у вопроса)
        parent_answer_id = None

        if question:
            if question.get_depth() > 1:
                parent_answer_id = question.get_parent().id

        return Response({
            "bot_answer": question.message,
            "answers": answers,
            "parent_answer_id": parent_answer_id
        })


