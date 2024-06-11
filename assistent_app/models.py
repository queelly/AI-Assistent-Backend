from ckeditor.fields import RichTextField
from django.db import models
from rest_framework.exceptions import PermissionDenied
from treebeard.mp_tree import MP_Node


# Create your models here.

class AssistentThemeModel(models.Model):
    title = models.CharField('Тема ассистента', max_length=256, null=True, blank=True)
    is_active = models.BooleanField("Тема активная?", default=True)

    class Meta:
        verbose_name = "Тема ассистента"
        verbose_name_plural = "Темы ассистента"

    def __str__(self):
        return self.title


class ChatMessageModel(MP_Node):
    theme = models.ForeignKey(to=AssistentThemeModel, verbose_name="Тема", null=True, blank=False,
                              on_delete=models.SET_NULL)

    is_active = models.BooleanField(verbose_name="Ветка сообщения активна?", default=True)

    message = RichTextField(verbose_name="Текст сообщения", null=True, blank=False)

    is_filter_question = models.BooleanField("Вопрос на фильтрацию товаров", default=True)

    class Meta:
        ordering = ['theme']
        verbose_name = "Дерево сообщений чата"

    def __str__(self):
        return self.message or ''

    class Meta:
        verbose_name = "Сообщение ассистента"
        verbose_name_plural = "Сообщения ассистента"


class FilterFields(models.Model):
    chat_message = models.ForeignKey(ChatMessageModel, null=False, blank=False, on_delete=models.CASCADE)
    field_name = models.CharField("Поле для фильтрации", max_length=50)
    many = models.BooleanField("Посылается множетсво значений?", default=False)
    message = RichTextField(verbose_name="Текст сообщения", null=True, blank=True)

    def __str__(self):
        return f'{self.field_name} - {self.message}'
    class Meta:
        verbose_name = "Фильтрация"
