import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def weight_limit_validator(value) -> None:
    if value > 500:
        raise ValidationError(
            _('%(value)s is too heavy for the drone'),
            params={'value': value},
        )


def medication_name_validator(name: str) -> None:
    match = re.fullmatch("[A-Za-z]*[0-9]*(_)*(-)*[A-Za-z]*[0-9]*", name)

    if not match:
        raise ValidationError(
            _('%(name)s is not valid. Allowed only letters, numbers, "-", "_"'),
            params={'name': name},
        )
