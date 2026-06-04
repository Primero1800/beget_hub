from modeltranslation.translator import TranslationOptions, register

from .models import SubProject


@register(SubProject)
class SubProjectTranslationOptions(TranslationOptions):
    fields = ("name", "description")
