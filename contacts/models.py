from django.db import models

# Create your models here.
from rest_framework.exceptions import ValidationError


def validate_mobile_number(value):
    mobile_number_str = str(value)
    if len(mobile_number_str) != 10:
        raise ValidationError("mobile number contains 10 digit ")
    return value


class Contact(models.Model):
    name = models.CharField(max_length=10,unique=True)
    email = models.EmailField(unique=True)
    mobile_number = models.BigIntegerField(validators=[validate_mobile_number], unique=True)
    address = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.name
