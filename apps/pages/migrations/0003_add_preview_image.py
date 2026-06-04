from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_add_mirror_subproject"),
    ]

    operations = [
        migrations.AddField(
            model_name="subproject",
            name="preview_images",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="List of up to 9 image URLs for 3×3 collage",
            ),
        ),
    ]
