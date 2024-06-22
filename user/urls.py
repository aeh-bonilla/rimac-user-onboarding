from django.urls import path
from . import views


# URLs de la app de onboarding de usuarios
urlpatterns = [
    path('gets', views.gets, name='gets'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('update/<int:user_id>', views.update, name='update'),
    path('delete/<int:user_id>', views.delete, name='delete'),
]
