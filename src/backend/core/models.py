from django.conf import settings
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from core.choices import ColorChoices


class Workspace(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name="Название",
        default="Workspace",
        null=False,
        blank=False,
        db_index=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(64)],
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="workspaces",
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Окружение"
        verbose_name_plural = "Окружения"

    def __str__(self):
        return "{}: {}".format(self.user.username, self.name)


class Tag(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name="Название",
        null=False,
        blank=False,
        db_index=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(64)],
    )
    color = models.CharField(
        max_length=32, default=ColorChoices.GRAY, choices=ColorChoices.choices
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        verbose_name="Окружение",
        related_name="tags",
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return "{}".format(self.name)


class Ticket(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок",
        validators=[MinLengthValidator(3), MaxLengthValidator(256)],
        null=False,
        blank=False,
        db_index=True,
    )
    description = models.TextField(
        max_length=2048,
        verbose_name="Описание",
        validators=[MaxLengthValidator(2048)],
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, null=False, blank=False
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        verbose_name="Окружение",
        related_name="tickets",
        null=False,
        blank=False,
    )
    tags = models.ManyToManyField(
        Tag, related_name="tickets", verbose_name="Теги", blank=True
    )

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"
        get_latest_by = "-created_at"
        ordering = ["-created_at"]

    def __str__(self):
        return "{}: {}".format(self.workspace.name, self.title)
