from django.conf import settings
from rest_framework import serializers

from core.models import Tag, Ticket, Workspace


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name", "color", "workspace")


class WorkspaceSerializer(serializers.ModelSerializer):
    ticket_count = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ("id", "name", "tags", "ticket_count")

    def get_ticket_count(self, obj):
        return obj.tickets.count()


class UserSerializer(serializers.ModelSerializer):
    workspaces = WorkspaceSerializer(many=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("id", "username", "email", "workspaces")


class TicketSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "title",
            "description",
            "created_at",
            "workspace",
            "tags",
        )

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        ticket = Ticket.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            ticket.tags.add(tag)
        ticket.save()
        return ticket
