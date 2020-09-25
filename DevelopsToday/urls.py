from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls"), name="api"),
    # path('swagger/', schema_view)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

schema_view = get_schema_view(
    openapi.Info(title="Backend API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=None),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=None),
        name="schema-redoc",
    ),
]
