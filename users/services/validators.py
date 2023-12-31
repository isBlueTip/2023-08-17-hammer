import re

from rest_framework.exceptions import ValidationError as DRFValidationError

from users import constants


def validate_otp(otp: str) -> bool:
    """
    Validates string as an otp format.
    """
    if not otp.isnumeric():
        raise DRFValidationError("OTP must be numeric")


def validate_phone(phone: str) -> None:
    """
    Validates string as a phone number format.
    """
    if not phone.isnumeric():
        raise DRFValidationError(constants.PHONE_VALIDATION_ERROR)

    if not re.match(constants.INTERNATIONAL_PHONE_REGEX, phone):
        raise DRFValidationError(constants.PHONE_VALIDATION_ERROR)
