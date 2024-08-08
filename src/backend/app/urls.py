from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

THIRD_PARTY_APPS_URLS = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/register/", include("dj_rest_auth.registration.urls")),
]

LOCAL_APPS_URLS = [path("api/", include("core.urls"))]

urlpatterns = (
    [
        path("admin/", admin.site.urls),
    ]
    + THIRD_PARTY_APPS_URLS
    + LOCAL_APPS_URLS
)
