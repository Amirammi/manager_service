# Generated by Django 4.1 on 2023-05-12 05:58

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("task_manager", "0003_position_duties"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
