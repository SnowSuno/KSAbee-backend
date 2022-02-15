import re

from tortoise import models, fields
from tortoise.validators import RegexValidator


class Student(models.Model):
    sid = fields.CharField(
        pk=True,
        max_length=6,
        validators=[RegexValidator(r"^\d\d-\d\d\d$", re.A)]
    )
    name = fields.CharField(max_length=20)
    # account
