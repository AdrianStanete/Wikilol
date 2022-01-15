from champions.models import Champion
from rest_framework import serializers


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ('name', 'hability_power')
