from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'champions', views.ChampionsView, basename='champions')
router.register(r'abilities', views.AbilitiesView, basename='abilities')
urlpatterns = router.urls

#urlpatterns = [
#    path('', include(router.urls)),
#]


#from rest_framework.routers import SimpleRouter
#from . import views

#router = SimpleRouter(trailing_slash=True)
#router.register(r'champions', views.ChampionsView, basename='champions')
#router.register(r'abilities', views.AbilitiesView, basename='abilities')
#urlpatterns = router.urls
