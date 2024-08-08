# Generated by Django 5.0.7 on 2024-08-07 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag_workspace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tickets', to='core.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='name',
            field=models.CharField(db_index=True, default='Workspace', max_length=64, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(64)], verbose_name='Название'),
        ),
    ]