from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Sale(models.Model):
    def __str__(self) -> str:
        return self.user_id.username

    created_at = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
