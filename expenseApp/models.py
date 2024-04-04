from django.db import models
from django.contrib.auth.models import User
# Create your models here.

mychoices=(
    ('loan-repayment','Loan-Repayment'),
    ('loan-given','Loan-Given'),
    ('uncategorized','Uncategorized'),
    ('food','Food'),
    ('travel','Travel'),
    ('salary','Salary'),
    ('income','Income'),
    ('fd','FD'),
    ('rd','RD'),
    ('invoice-payment','Inovice-Payment')
)
transaction_choice=(
    ('added','Credit'),
    ('debit','Debit')
)

class transaction(models.Model):
    user = models.ForeignKey(to=User ,on_delete=models.CASCADE)
    paid_for = models.CharField(max_length=40, default='Unknown', null=True)
    amount = models.BigIntegerField(null=False, default=0)
    transaction_type = models.CharField(max_length=20, choices=transaction_choice, default='debit', null=False)
    category = models.CharField(max_length=15, default='food', choices=mychoices)
    paid_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.paid_for)
