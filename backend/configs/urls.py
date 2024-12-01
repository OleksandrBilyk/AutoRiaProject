from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='CloneAutoRia',
        default_version='v2.2',
        description='Project Like Autoria',
        contact=openapi.Contact(email='biluksanya@ukr.net')
    ),
    public=True,
    permission_classes=[AllowAny,],
)
urlpatterns = [
    path('api/users', include('apps.users.urls')),
    path('api/auth', include('apps.auth.urls')),
    path('api/cars', include('apps.cars.urls')),
    path('api/information', include('apps.information.urls')),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='documentation'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
