from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from core import filters
from core.models import Tag, Ticket, Workspace
from core.serializers import TagSerializer, TicketSerializer, WorkspaceSerializer


class WorkspaceViewSet(ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workspace.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = filters.TagFilter


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all().order_by("-created_at")
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = filters.TicketFilter
