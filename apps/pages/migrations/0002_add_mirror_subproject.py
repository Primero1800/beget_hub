from django.db import migrations


def add_mirror_subproject(apps, schema_editor):
    SubProject = apps.get_model("pages", "SubProject")
    SubProject.objects.create(
        name="Mirror",
        name_ru="Зеркало",
        name_en="Mirror",
        url="https://mirror.primero1800.ru",
        description_ru="Webcam-зеркало с визуализатором звука",
        description_en="Webcam mirror with audio visualizer",
        order=1,
        active=True,
    )


def remove_mirror_subproject(apps, schema_editor):
    SubProject = apps.get_model("pages", "SubProject")
    SubProject.objects.filter(url="https://mirror.primero1800.ru").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_mirror_subproject, remove_mirror_subproject),
    ]
