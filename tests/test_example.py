from django.test import Client

import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_homepage():
    client = Client()  # Create an instance of Django's test client
    url = reverse('world')
    response = client.get(url)
    assert response.status_code == 200