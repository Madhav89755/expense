from django.db import models
from django.contrib.auth.models import User
from utils.choices import (
    TRANSACTION_CATEGORY_CHOICES, 
    TRANSACTION_CATEGORY_CHOICE_FOOD,
    TRANSACTION_TYPE_CHOICES,
    TRANSACTION_TYPE_CHOICE_DEBIT)
# Create your models here.

class transaction(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    paid_for = models.CharField(max_length=40, default='Unknown')
    amount = models.BigIntegerField(default=0)
    transaction_type = models.CharField(max_length=20,
                                        choices=TRANSACTION_TYPE_CHOICES,
                                        default=TRANSACTION_TYPE_CHOICE_DEBIT)
    category = models.CharField(max_length=15,
                                default=TRANSACTION_CATEGORY_CHOICE_FOOD,
                                choices=TRANSACTION_CATEGORY_CHOICES)
    paid_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.paid_for)
