from django.urls import include, path
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r"tags", views.TagViewSet)
router.register(r"tickets", views.TicketViewSet)
router.register(r"workspaces", views.WorkspaceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
