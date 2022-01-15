import requests
from rest_framework import status
import pytest

# Create your tests here.
@pytest.mark.django_db
class TestAbilities:
    def test_creates_ability_when_data_is_valid(self, client, champion):
        data = {'name': 'Razor Shuriken',
                'description': 'Does this and that',
                'power': 5,
                'champion': champion.id}
        response = client.post('/abilities/', data)

        assert response.status_code == status.HTTP_201_CREATED
