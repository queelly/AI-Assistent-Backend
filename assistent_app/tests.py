from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.test import TestCase
from rest_framework.request import Request

from assistent_app.models import AssistentThemeModel, ChatMessageModel, FilterFields, FilterConfig
from assistent_app.services import FactoryState, ThemeList, ThemeQuestionsList, AnswerAcceptState, FilterAnswerAccept

import logging

from assistent_app.views import FilterSuggestionSerializer
from core.models import InvestPlace

logger = logging.getLogger(__name__)


class ChatCasetTest(TestCase):
    def setUp(self) -> None:
        get = lambda node_id: ChatMessageModel.objects.get(pk=node_id)

        theme1 = AssistentThemeModel.objects.create(title="Первая тема")
        theme2 = AssistentThemeModel.objects.create(title="Вторая тема")

        root1 = ChatMessageModel.add_root(theme=theme1, message="Первое сообщение?")
        node = get(root1.pk).add_child(message="Ответ на сообщение1")

        answer1 = node.add_child(message="Ебаный рот", is_filter_question=True)

        filter_config = FilterConfig.objects.create(model_class=AssistentThemeModel)

        FilterFields.objects.create(model_class=filter_config, field_name="one_filter", choices="choices,bred",
                                    message="Бред")

        get(node.pk).add_sibling(message="Ответ2 на сообщение1")

        root2 = ChatMessageModel.add_root(theme=theme2, message="Второе сообщение?")
        node2 = get(root2.pk).add_child(message="Ответ на сообщение1")
        get(node.pk).add_sibling(message="Ответ2 на сообщение1")

    class TestRequest:
        data = {}

        def __init__(self, data):
            self.data = data

    def test_show_list_themes(self):
        request = ChatCasetTest.TestRequest({"theme": True})

        state = FactoryState.create_chat_option(request)

        self.assertIsInstance(state, (ThemeList,))

        result = state.result()

        logger.info("Result state ThemeList: %s", result)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['text'], "Первая тема")
        self.assertEqual(result[1]['text'], "Вторая тема")

    def test_show_theme_question(self):
        request = ChatCasetTest.TestRequest({"theme_id": 1})

        state = FactoryState.create_chat_option(request)

        self.assertIsInstance(state, (ThemeQuestionsList,))

        question_list = state.result()

        logger.info("Result state ThemeQuestionList: %s", question_list)

        self.assertEqual(len(question_list), 1)
        self.assertEqual(question_list['answers'][0]['answer_text'], "Первое сообщение?")

    def test_on_select_first_question(self):
        request = ChatCasetTest.TestRequest({"answer_id": 1})

        state = FactoryState.create_chat_option(request)

        self.assertIsInstance(state, (AnswerAcceptState,))

        logger.info("Answered on selected question: %s", state.result())

    def test_select_filter_question(self):
        request = ChatCasetTest.TestRequest({"answer_id": 3})

        state = FactoryState.create_chat_option(request)

        self.assertIsInstance(state, (FilterAnswerAccept,))

        logger.info("Answered on selected question: %s", state.result())
