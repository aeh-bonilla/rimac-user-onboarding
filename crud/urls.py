from django.contrib import admin
from django.urls import path, include


# URLs globales
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('user.urls'))
]
