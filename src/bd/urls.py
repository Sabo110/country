from rest_framework.routers import DefaultRouter

from .views import SalleViewset, EtudiantViewset

router = DefaultRouter()
router.register('salle', SalleViewset)
router.register('etudiant', EtudiantViewset)
urlpatterns = router.urls