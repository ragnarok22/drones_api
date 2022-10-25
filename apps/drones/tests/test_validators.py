from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.drones.validators import medication_name_validator


class ValidatorTestCase(TestCase):
    def test_medication_name(self):
        medication_name_validator("DIPIRONA12")
        medication_name_validator("45Aspirine")
        self.assertIsNone(medication_name_validator("Dipirone_45"))

    def test_medication_name_fail(self):
        with self.assertRaises(ValidationError):
            medication_name_validator("NOT*A*MEDICATION")
