from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
    openapi.Info(
        title="Comments API",
        default_version="v1",
    ),
    public=True,
)

urlpatterns = [
    re_path(
        r"^swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
