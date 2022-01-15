import requests
from rest_framework import status
from django.test import TestCase
import pytest


# Create your tests here.

@pytest.mark.django_db
class TestRetriveChampion:
    def test_returns_champion_when_it_exists(self, client, champion):
        response = client.get(f'/champions/{champion.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'name': 'Yasuo', 'hability_power': 10}


@pytest.mark.django_db
class TestCreateChampion:
    def test_creates_champion_when_data_is_valid(self, client):
        data = {'name': 'zed', 'hability_power': 5}
        response = client.post('/champions/', data)

        assert response.status_code == status.HTTP_201_CREATED

    def test_does_not_create_champion_when_name_is_used(self, client, champion):
        data = {"name": champion.name, 'hability_power': 50}
        response = client.post(f'/champions/', data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


# <-------------------------------HOMEWORK 2,3,4------------------------------->
# Añado mixin de Patch

@pytest.mark.django_db
class TestEditChampion:
    def test_modify_hability_power(self, client, champion):
        response = client.patch(f'/champions/', champion.hability_power)

        if response in range(1, 100):
            return response
            assert response.status_code == status.HTTP_200_OK  # algo pasa con esta linea
        else:
            assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_does_not_modify_champion_name(self, client, champion):
        response = client.patch(f'/champions/', champion.name)

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


# <-------------------------------END HOMEWORK 2,3,4------------------------------->

@pytest.mark.django_db
class TestListChampion:
    def test_returns_champions_when_champions_exist(self, client, champions):
        response = client.get('/champions/')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [{'name': 'Yasuo', 'hability_power': 10}, {'name': 'Zed', 'hability_power': 7}]

    # <-------------------------------HOMEWORK 1------------------------------->
    def test_no_retrieving_list_exists(self, client):
        response = client.get('')

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_no_champion_exists(self, client):
        response = client.get('/champions/')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []


# <-------------------------------END HOMEWORK 1------------------------------->
