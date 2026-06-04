from django.conf import settings
from django.shortcuts import render

from .models import SubProject


def hub_index(request):
    projects = SubProject.objects.filter(active=True)
    return render(
        request,
        "pages/index.html",
        {
            "projects": projects,
            "version": settings.VERSION,
        },
    )
