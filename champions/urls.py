from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter(trailing_slash=True)
router.register('', views.ChampionsView, basename='champions')
urlpatterns = router.urls
