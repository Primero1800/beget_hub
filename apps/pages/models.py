from django.db import models


class SubProject(models.Model):  # type: ignore[django-manager-missing]
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self) -> str:
        return str(self.name)


class PreviewImage(models.Model):
    subproject = models.ForeignKey(
        SubProject, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="previews/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return f"{self.subproject.name} #{self.pk}"
