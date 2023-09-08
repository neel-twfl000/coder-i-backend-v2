from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Ecommerence Developer Zone')

urlpatterns = [
    path('db/', admin.site.urls),
    path('swagger/', schema_view, name="swagger"),
    path('', include('v1.home.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
