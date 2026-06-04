from django.conf import settings
from django.shortcuts import render

PROJECTS: list[dict[str, str]] = [
    # {"name": "Football", "url": "https://football.primero1800.ru", "description": ""},
]


def hub_index(request):
    return render(
        request,
        "pages/index.html",
        {
            "projects": PROJECTS,
            "version": settings.VERSION,
        },
    )
