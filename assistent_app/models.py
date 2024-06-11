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
    theme = models.ForeignKey(to=AssistentThemeModel, null=True, blank=False, on_delete=models.SET_NULL)

    is_active = models.BooleanField(verbose_name="Ветка сообщения активна?", default=True)

    message = RichTextField(verbose_name="Текст сообщения", null=True, blank=False)

    def delete(self, *args, **kwargs):
        if self.is_root():
            raise PermissionDenied('Cannot delete root topic')

        super(ChatMessageModel, self).delete()

    def __str__(self):
        return self.message or ''

    class Meta:
        verbose_name = "Сообщение ассистента"
        verbose_name_plural = "Сообщения ассистента"

