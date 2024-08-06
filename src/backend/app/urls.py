from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static


THIRD_PARTY_APPS_URLS = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("auth/", include("dj_rest_auth.urls")),
]

LOCAL_APPS_URLS = []

urlpatterns = (
    [
        path("admin/", admin.site.urls),
    ]
    + THIRD_PARTY_APPS_URLS
    + LOCAL_APPS_URLS
)
