from django.shortcuts import render
from django.conf import settings


PROJECTS = [
    # {"name": "Football", "url": "https://football.primero1800.ru", "description": "..."},
]


def hub_index(request):
    return render(request, "pages/index.html", {
        "projects": PROJECTS,
        "version": settings.VERSION,
    })
