from django.test import TestCase

import requests

BASE_URI='http://localhost:8000/api/v1/employee/'
class EmployeeTest(TestCase):

    def test_noofemps(self):
        response = requests.get(BASE_URI)
        self.assertEqual(len(response.json()),3)

        empjson = {
                "name": "PQRS",
                "age": 23,
                "salary": 43230,
                "position": "Manager",
                "gender": "Male",
                "active": "Y"
                }
        response = requests.post(BASE_URI,json=empjson)
        self.assertEqual(response.status_code,201)
        response = requests.get(BASE_URI)

        self.assertEqual(len(response.json()), 4)
        self.assertEqual(response.json()[-1]["position"],'Manager')
