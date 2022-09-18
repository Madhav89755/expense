from django import forms  
from .models import transaction  
  
class transactionForm(forms.ModelForm):  
    class Meta:  
        model = transaction  
        fields = ['paid_for','amount','transaction_type','category']
        widgets={
            'paid_for':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'transaction_type':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }