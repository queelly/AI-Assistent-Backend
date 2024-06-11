from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from assistent_app.models import AssistentThemeModel, ChatMessageModel, FilterFields


# Register your models here.

@admin.register(AssistentThemeModel)
class AssistentTheme(admin.ModelAdmin):
    pass


class FieldsFilterAdmin(admin.StackedInline):
    model = FilterFields


@admin.register(ChatMessageModel)
class AssistPromptAdmin(TreeAdmin):
    change_form_template = 'change_form.html'
    list_display = ['message', 'theme', 'is_active']
    inlines = [FieldsFilterAdmin, ]
    form = movenodeform_factory(ChatMessageModel)
