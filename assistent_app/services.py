from abc import ABC

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from assistent_app.models import AssistentThemeModel, ChatMessageModel, FilterFields
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
    def __init__(self, theme):
        self.theme_parent = theme

    def result(self):
        if not self.theme_parent:
            raise ValidationError("Данная тема не найдена")

        questions = ChatMessageModel.objects.filter(theme=self.theme_parent, depth=1)

        response_data = []
        for question in questions:
            response_data.append({
                "id": question.id,
                "answer_text": question.message,
            })

        return {
            "answers": response_data
        }


class AnswerAcceptState(DecisionAssistentState):
    def __init__(self, answer_node):
        self.answer_node = answer_node

    def result(self):
        if not self.answer_node:
            return ValidationError('Данный ответ не предусмотрен!')

        question = self.answer_node.get_parent()

        answer_node = self.answer_node.get_first_child()

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


class FilterAnswerAccept(DecisionAssistentState):
    def __init__(self, answer_node):
        self.answer_node = answer_node

    def result(self):
        if not self.answer_node or not self.answer_node.is_filter_question:
            raise ValidationError('Не найден ответ на данный вопрос')

        if not self.answer_node.filter_model:
            raise ValidationError('filter model')

        question = self.answer_node.get_parent()

        filter_fields = FilterFields.objects.filter(model_class=self.answer_node.filter_model)

        parent_answer_id = None

        filters = []

        for filter in filter_fields:
            filters.append({
                "field_name": filter.field_name,
                "many": filter.many,
                "choices": filter.choices,
                "message": filter.message
            })

        if question:
            if question.get_depth() > 1:  # Проверяем, есть ли родитель у вопроса
                parent_answer_id = question.get_parent().id

        return {
            "send_id": self.answer_node.filter_model.id,
            "parent_answer_id": parent_answer_id,
            "filters": filters
        }


class FactoryState:
    @staticmethod
    def create_chat_option(request):
        theme = request.data.get("theme", False)

        #Запрос тем
        if theme:
            return ThemeList()

        theme_id = request.data.get('theme_id', None)

        #Запрос вопросов
        if theme_id:
            return ThemeQuestionsList(theme=get_object_or_none(AssistentThemeModel, id=theme_id))

        answer_id = request.data.get('answer_id', None)


        #Обработка ответа
        if answer_id:
            answer = get_object_or_none(ChatMessageModel, id=answer_id)

            #ответ должен ввести к фильтрации какой-то :/
            if answer.is_filter_question:
                return FilterAnswerAccept(answer)
            else:
                return AnswerAcceptState(answer)

        raise ValidationError("Не правильно указаны данные")