from django.urls import path, include

urlpatterns = [
    path('api/', include('v1.home.api.urls'))
]