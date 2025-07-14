from django.db import models
from django.core.validators import EmailValidator

class EmailData(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

