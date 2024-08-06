from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

class HealthCheckTests(TestCase):
    def test_health_check(self):
        client = APIClient()
        url = reverse('health_check')
        res = client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
