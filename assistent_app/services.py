from abc import ABC

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from assistent_app.models import AssistentThemeModel, ChatMessageModel
from assistent_project.utils import get_object_or_none


class DecisionAssistentState(ABC):
    def result(self):
        pass


class ThemeList(DecisionAssistentState):
    def result(self):
        response = []

        themes = AssistentThemeModel.objects.filter(is_active=True)

        for theme in themes:
            response.append({"id": theme.id, "text": theme.title})

        return response


class ThemeQuestionsList(DecisionAssistentState):
    def __init__(self, theme_id):
        self.theme_id = theme_id

    def result(self):
        theme_parent = get_object_or_none(AssistentThemeModel, id=self.theme_id)

        if not theme_parent:
            raise ValidationError("Данная тема не найдена")

        questions = ChatMessageModel.objects.filter(theme=theme_parent, depth=1)

        response_data = []
        for question in questions:
            response_data.append({
                "answer_id": question.id,
                "answer_text": question.message,
            })

        return response_data


class AnswerAcceptState(DecisionAssistentState):
    def __init__(self, answer_id):
        self.answer_id = answer_id

    def result(self):
        answer_node = get_object_or_none(AssistentThemeModel, id=self.answer_id)

        if not answer_node:
            return ValidationError('Данный ответ не предусмотрен!')

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

        return {
            "bot_answer": answer_node.message,
            "answers": answers,
            "parent_answer_id": parent_answer_id
        }

