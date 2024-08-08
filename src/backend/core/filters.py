from django_filters import rest_framework as filters

from core.models import Tag, Ticket


class TicketFilter(filters.FilterSet):

    class Meta:
        model = Ticket
        fields = {"workspace__id": ["exact"], "created_at": ["lte", "gte", "exact"]}


class TagFilter(filters.FilterSet):
    class Meta:
        model = Tag
        fields = {"workspace": ["exact"], "name": ["icontains"], "color": ["exact"]}
