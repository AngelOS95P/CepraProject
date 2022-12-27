from rest_framework import routers
from django.urls import path, include
from .viewsets import SesionViewSet, PelucheViewSet, TableroViewSet, VaritaViewSet, JuegoToposViewSet, JuegoRompeCViewSet, JuegoLaberintoViewSet, JuegoLetrasCViewSet, JuegoColorearViewSet

router = routers.SimpleRouter()
router.register(r'sesion', SesionViewSet)
router.register(r'peluche', PelucheViewSet)
router.register(r'tablero', TableroViewSet)
router.register(r'varita', VaritaViewSet)
router.register(r'topos', JuegoToposViewSet)
router.register(r'colorear', JuegoColorearViewSet)
router.register(r'rompeC', JuegoRompeCViewSet)
router.register(r'laberinto', JuegoLaberintoViewSet)
router.register(r'letras', JuegoLetrasCViewSet)


urlpatterns = router.urls