from rest_framework import routers
from django.urls import path, include
from .viewsets import RecoPelucheViewSet,RecoJuegosSViewSet, RecoTableroViewSet, RecoVaritaViewSet

router = routers.SimpleRouter()
router.register(r'ReJuegos', RecoJuegosSViewSet)
router.register(r'RePeluche', RecoPelucheViewSet)
router.register(r'ReVarita', RecoVaritaViewSet)
router.register(r'ReTablero', RecoTableroViewSet)

urlpatterns = router.urls