from django.db import models

# Create your models here.

mychoices=(
    ('uncategorized','uncategorized'),
    ('food','food'),
    ('snacks','snacks'),
    ('drinks','drinks'),
    ('travel','travel'),
    ('needs','needs'),
    ('salary','salary'),
    ('income','income')
)
transaction_choice=(
    ('added','added'),
    ('debit','debit')
)

class transaction(models.Model):
    paid_for = models.CharField(max_length=40, default='Unknown', null=True)
    amount = models.BigIntegerField(null=False)
    transaction_type = models.CharField(max_length=20, choices=transaction_choice, null=False)
    category = models.CharField(max_length=15, default='uncategorized', choices=mychoices)
    paid_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.paid_for)
