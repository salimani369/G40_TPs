from django.urls import include, path
from rest_framework import routers
from . import views

# Le router génère automatiquement toutes les URLs REST (GET, POST, PUT, DELETE)
router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    # URLs de l'API messages
    path('', include(router.urls)),
    # URLs d'authentification fournies par rest_framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]