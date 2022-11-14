from rest_framework.schemas import get_schema_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
# from rest_framework.schemas.coreapi import SchemaGenerator
from rest_framework.settings import api_settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from delivery.schemas import OpenApiBaseAuth
from django.views.decorators.cache import never_cache


urlpatterns = [
    path('openapi/', never_cache(get_schema_view(
        title="api for the tbot",
        description="api for viewing and ordering goods",
        version="1.0.0",
        renderer_classes=[OpenApiBaseAuth]
    )), name='openapi-schema'),
    path('api/v1/', include('menu.urls')),
    path('api/v1/', include('order.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
