import json

from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from django.urls import reverse
from rest_framework import status
from apps.drones.models import Drone, Medication


class DroneTests(APITestCase):
    def test_create_drone(self):
        """Ensure we can register a new drone"""
        url = reverse("drone-list")
        data = {
            'serial_number': 'SerialDroid',
            'model': 'Lightweight',
            'weight_limit': 256,
            'battery_capacity': 100,
            'state': 'IDLE'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Drone.objects.count(), 1)
        self.assertEqual(Drone.objects.get().serial_number, data.get('serial_number'))
        # 9 attr (id, serial_number, model, weight_limit, free_weight, occupied_weight, battery_capacity,
        # stat, medications)
        self.assertEqual(len(response.data), 9)

    def test_register_drone_with_wrong_state(self):
        url = reverse("drone-list")
        data = {
            'serial_number': 'SerialDroid',
            'model': 'Lightweight',
            'weight_limit': 256,
            'battery_capacity': 100,
            'state': 'Wrong'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('state')[0].code, 'invalid_choice')
        self.assertEqual(str(response.data.get('state')[0]), '"Wrong" is not a valid choice.')

    def test_get_drone_list(self):
        url = reverse("drone-list")

        # Create a Drone
        data = {
            'serial_number': 'SerialDroid',
            'model': 'Lightweight',
            'weight_limit': 256,
            'battery_capacity': 100,
            'state': 'IDLE'
        }
        drone = Drone.objects.create(**data)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content).get('count'), 1)
        self.assertEqual(json.loads(response.content).get('next'), None)
        self.assertEqual(json.loads(response.content).get('previous'), None)
        self.assertEqual(len(json.loads(response.content).get('results')), 1)
        self.assertEqual(json.loads(response.content).get('results')[0]['id'], drone.id)

    def test_drone_detail(self):
        url = reverse("drone-detail", args=[1, ])
        # Create a Drone
        data = {
            'serial_number': 'SerialDroid',
            'model': 'Lightweight',
            'weight_limit': 256,
            'battery_capacity': 100,
            'state': 'IDLE'
        }
        drone = Drone.objects.create(**data)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), drone.id)
        self.assertEqual(response.data.get('serial_number'), drone.serial_number)
        self.assertEqual(response.data.get('model'), drone.model)

    def test_non_exists_drone_detail(self):
        url = reverse("drone-detail", args=[1, ])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drone_available(self):
        url = reverse("drone-available")
        # Create a Drone
        data = {
            'serial_number': 'LazyDroid',
            'model': 'Lightweight',
            'weight_limit': 256,
            'battery_capacity': 100,
            'state': 'IDLE'
        }
        drone = Drone.objects.create(**data)
        data2 = {
            'serial_number': 'BusyDroid',
            'model': 'Lightweight',
            'weight_limit': 200,
            'battery_capacity': 90,
            'state': 'LOADING'
        }
        drone2 = Drone.objects.create(**data2)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = json.loads(response.content)

        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].get('id'), drone.id)
        self.assertNotEqual(response[0].get('id'), drone2.id)

    def test_drone_battery(self):
        url = reverse("drone-battery", args=[1, ])
        # Create a Drone
        data = {
            'serial_number': 'SerialDroid',
            'model': 'Lightweight',
            'weight_limit': 256,
            'battery_capacity': 50,
            'state': 'IDLE'
        }
        drone = Drone.objects.create(**data)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, drone.battery_capacity)

    def test_drone_medications(self):
        url = reverse("drone-medications", args=[1, ])
        # Create a Drone
        data = {
            'serial_number': 'SerialDroid',
            'model': 'Lightweight',
            'weight_limit': 256,
            'battery_capacity': 50,
            'state': 'IDLE'
        }
        Drone.objects.create(**data)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
