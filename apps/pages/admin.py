from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import SubProject


@admin.register(SubProject)
class SubProjectAdmin(TabbedTranslationAdmin):
    list_display = ["name", "url", "active", "order"]
    list_editable = ["active", "order"]
