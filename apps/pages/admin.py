from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import PreviewImage, SubProject


class PreviewImageInline(admin.TabularInline):
    model = PreviewImage
    extra = 3
    fields = ["image", "order"]


@admin.register(SubProject)
class SubProjectAdmin(TabbedTranslationAdmin):
    list_display = ["name", "url", "active", "order"]
    list_editable = ["active", "order"]
    inlines = [PreviewImageInline]
