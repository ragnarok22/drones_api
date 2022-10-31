from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.drones.validators import medication_name_validator, medication_code_validator, weight_limit_validator


class ValidatorTestCase(TestCase):
    def test_medication_name(self):
        medication_name_validator("DIPIRONA12")
        medication_name_validator("45Aspirine")
        self.assertIsNone(medication_name_validator("Dipirone_45"))

    def test_medication_name_fail(self):
        with self.assertRaises(ValidationError):
            medication_name_validator("NOT*A*MEDICATION")

    def test_medication_code(self):
        medication_code_validator("CODE123")
        medication_code_validator("123CODE")
        self.assertIsNone(medication_name_validator("DRONE_CODE"))

    def test_medication_code_fail(self):
        with self.assertRaises(ValidationError):
            medication_code_validator("CodeInvalid")

    def test_weight_limit(self):
       weight_limit_validator(430) 
       weight_limit_validator(130)
       weight_limit_validator(500)

    def test_weight_limit_fail(self):
        with self.assertRaises(ValidationError):
            weight_limit_validator(550)
