from champions.models import Champion
import pytest

@pytest.fixture()
def champion():
    return Champion.objects.create(name='Yasuo', hability_power=10)

@pytest.fixture()
def champions():
    return [Champion.objects.create(name='Yasuo', hability_power=10),
            Champion.objects.create(name='Zed', hability_power=7)]
