from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
]

urlpatterns += i18n_patterns(  # type: ignore[arg-type]
    path("admin/", admin.site.urls),
    path("", include("apps.pages.urls")),
)
