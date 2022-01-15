from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter(trailing_slash=True)
router.register('', views.AbilitiesView, basename='abilities')
urlpatterns = router.urls