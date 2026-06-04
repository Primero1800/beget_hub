from django.db import models


class SubProject(models.Model):  # type: ignore[django-manager-missing]
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(blank=True)
    preview_image = models.URLField(
        blank=True, help_text="URL of card preview screenshot"
    )
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self) -> str:
        return str(self.name)
