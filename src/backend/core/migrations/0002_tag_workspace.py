# Generated by Django 5.0.7 on 2024-08-07 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="workspace",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to="core.workspace",
                verbose_name="Окружение",
            ),
            preserve_default=False,
        ),
    ]