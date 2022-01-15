from rest_framework import mixins, viewsets
from abilities.models import Ability
from abilities.serializers import AbilitySerializer


# Create your views here.

class AbilitiesView(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer