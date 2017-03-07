from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_content(value):
    content = value
    if content == "abc":
        raise ValidationError("Content cannot be abc")
    return value
