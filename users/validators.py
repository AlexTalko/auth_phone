import re

from rest_framework.exceptions import ValidationError


def phone_validator(string):
    phone = re.sub(r'\b\D', '', string)
    clear_phone = re.sub(r'[\ \(]?', '', phone)
    if re.findall(r'^[\+7]*?\d{10}$' , clear_phone) or re.match(r'^[78]?\d{10}$', string):
        # print(phone, clear_phone)
        return True
    else:
        raise ValidationError('Укажите номер телефона в формате 79991233221')
