from rest_framework import routers

from .viewsets import EstudianteViewSet, EvaluacionViewSet

router = routers.SimpleRouter()
router.register('estudiante', EstudianteViewSet)
router.register('evaluacion', EvaluacionViewSet)

urlpatterns = router.urls