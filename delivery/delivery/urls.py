from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from delivery.schemas import OpenApiBaseAuth


urlpatterns = [
    path('openapi/', get_schema_view(
        title="api for the tbot",
        description="api for viewing and ordering goods",
        version="1.0.0",
        renderer_classes=[OpenApiBaseAuth]
    ), name='openapi-schema'),
    path('api/v1/', include('menu.urls')),
    path('api/v1/', include('order.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
