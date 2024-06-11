from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from assistent_app.models import AssistentThemeModel, ChatMessageModel


# Register your models here.

@admin.register(AssistentThemeModel)
class AssistentTheme(admin.ModelAdmin):
    pass


@admin.register(ChatMessageModel)
class AssistPromptAdmin(TreeAdmin):
    list_display = ['message', 'theme', 'is_active']
    form = movenodeform_factory(ChatMessageModel)


