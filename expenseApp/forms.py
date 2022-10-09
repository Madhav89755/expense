from django import forms  
from .models import transaction  
  
class transactionForm(forms.ModelForm):  
    class Meta:  
        model = transaction  
        fields = ['paid_for','amount','transaction_type','category']
        widgets={
            'paid_for':forms.TextInput(attrs={'class':'form-control','id':'paid_id'}),
            'amount':forms.NumberInput(attrs={'class':'form-control','id':'amount_id'}),
            'transaction_type':forms.Select(attrs={'class':'form-control','id':'transaction_id'}),
            'category':forms.Select(attrs={'class':'form-control','id':'category_id'}),
        }