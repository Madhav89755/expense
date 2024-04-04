from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from utils.choices import (
    TRANSACTION_CATEGORY_CHOICES, 
    TRANSACTION_CATEGORY_CHOICE_FOOD,
    TRANSACTION_TYPE_CHOICES,
    TRANSACTION_TYPE_CHOICE_DEBIT)
# Create your models here.

class transaction(models.Model):
    user = models.ForeignKey(verbose_name=_("User"),
                             to=User,
                             on_delete=models.CASCADE)
    paid_for = models.CharField(verbose_name=_("Title"),
                                max_length=40,
                                default='Unknown')
    amount = models.BigIntegerField(verbose_name=_("Transaction Amount"),
                                    default=0)
    transaction_type = models.CharField(verbose_name=_("Transaction Type"),
                                        max_length=20,
                                        choices=TRANSACTION_TYPE_CHOICES,
                                        default=TRANSACTION_TYPE_CHOICE_DEBIT)
    category = models.CharField(verbose_name=_("Transaction Category"),
                                max_length=15,
                                default=TRANSACTION_CATEGORY_CHOICE_FOOD,
                                choices=TRANSACTION_CATEGORY_CHOICES)
    paid_on = models.DateTimeField(verbose_name=_("Transaction Date"),
                                   auto_now_add=True)
    
    @property
    def relevant_transaction_type(self):
        for x in TRANSACTION_TYPE_CHOICES:
            if x[0]==self.transaction_type:
                return x[1]
        return self.transaction_type
    
    @property
    def relevant_transaction_category(self):
        for x in TRANSACTION_CATEGORY_CHOICES:
            if x[0]==self.category:
                return x[1]
        return self.category
    
    def __str__(self):
        return str(self.paid_for)
