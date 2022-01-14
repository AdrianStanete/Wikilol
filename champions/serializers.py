from champions.models import Champion
from champions.models import Ability
from rest_framework import serializers


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ('name', 'hability_power')


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ('name', 'description', 'power', 'champion')
