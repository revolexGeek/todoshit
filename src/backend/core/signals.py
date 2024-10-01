from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Workspace


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_workspace_for_new_user(sender, instance, created, **kwargs):
    if created:
        Workspace.objects.create(user=instance, name="Workspace 1")
