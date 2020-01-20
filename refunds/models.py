from django.db import models
from django.conf import settings
#from ecommerce.models import Order

# Create your models here.
class Refund(models.Model):
    order = models.ForeignKey('ecommerce.Order', on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"

