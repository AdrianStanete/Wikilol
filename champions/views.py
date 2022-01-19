from django.shortcuts import render
from rest_framework import mixins, viewsets
from champions.models import Champion
from abilities.models import Ability
from champions.serializers import ChampionSerializer
from abilities.serializers import AbilitySerializer


# Create your views here.

class ChampionsView(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

class AbilitiesView(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
