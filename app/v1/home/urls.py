from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('api/', include('v1.home.api.urls'))
]