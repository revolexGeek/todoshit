from django.contrib import admin

from core.models import Tag, Ticket, Workspace


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "tickets")
    list_filter = ("user",)

    def tickets(self, obj):
        return obj.tickets.count()


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "workspace", "_tags", "created_at")
    readonly_fields = ("created_at",)
    list_filter = ("workspace__name",)

    def _tags(self, obj):
        return ",".join([tag.name for tag in obj.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "color")
    list_filter = ("name",)
