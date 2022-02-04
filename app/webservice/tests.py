from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import *


# Create your tests here.
class VpsTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('webservice.urls')),
    ]
    
    def test_create_account(self):
        url = reverse('methodapi')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_create_vps(self):
        url = reverse('methodapi')
        data = {
          'data': {
            'cpu': 8,
            'ram': 1024,
            'hdd': 3,
            'status': 2
          }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vps.objects.count(), 1)
        self.assertEqual(Vps.objects.get().cpu, 8)
        self.assertEqual(Vps.objects.get().ram, 1024)
        self.assertEqual(Vps.objects.get().hdd, 3)
        self.assertEqual(Vps.objects.get().status, 2)


    def test_find_vps(self):
        url = reverse('methodapi')
        vps1 = Vps.objects.create(cpu=4, ram=256, hdd=1, status=0)
        rez1 = {"id": str(vps1.id), "cpu": 4, "ram": 256, "hdd": 1, "status": 0}

        vps2 = Vps.objects.create(cpu=6, ram=512, hdd=2, status=1)
        rez2 = {"id": str(vps2.id), "cpu": 6, "ram": 512, "hdd": 2, "status": 1}

        vps3 = Vps.objects.create(cpu=8, ram=1024, hdd=3, status=2)
        rez3 = {"id": str(vps3.id), "cpu": 8, "ram": 1024, "hdd": 3, "status": 2}

        vps4 = Vps.objects.create(cpu=16, ram=512, hdd=1, status=0)
        rez4 = {"id": str(vps4.id), "cpu": 16, "ram": 512, "hdd": 1, "status": 0}
        
        filter1 = {
            'cpu': 4
        }
        response1 = self.client.get(url, filter1)
        response1.render()
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertTrue(rez1 in response1.json())

        filter2 = {
            'ram': 512
        }
        response2 = self.client.get(url, filter2)
        response2.render()
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertTrue(rez2 in response2.json())
        self.assertTrue(rez4 in response2.json())

        filter3 = {
            'hdd': 3
        }
        response3 = self.client.get(url, filter3)
        response3.render()
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        self.assertTrue(rez3 in response3.json())

        filter4 = {
            'status': 0
        }
        response4 = self.client.get(url, filter4)
        response4.render()
        self.assertEqual(response4.status_code, status.HTTP_200_OK)
        self.assertTrue(rez4 in response4.json())
        self.assertTrue(rez1 in response4.json())

        filter_uid = {
            'uid': str(vps4.id)
        }
        response_uid = self.client.get(url, filter_uid)
        response_uid.render()
        self.assertEqual(response_uid.status_code, status.HTTP_200_OK)
        self.assertTrue(rez4 in response_uid.json())

    
    def test_set_status_vps(self):
        url = reverse('methodapi')
        vps = Vps.objects.create(cpu=4, ram=256, hdd=1, status=0)

        data = {
            'uid': str(vps.id),
            'status': 2
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vps.objects.count(), 1)
        self.assertEqual(Vps.objects.get().cpu, 4)
        self.assertEqual(Vps.objects.get().ram, 256)
        self.assertEqual(Vps.objects.get().hdd, 1)
        self.assertEqual(Vps.objects.get().status, 2)
