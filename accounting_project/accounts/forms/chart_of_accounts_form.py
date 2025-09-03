from django import forms
from ..models.chart_of_account import ChartOfAccount

class ChartOfAccountForm(forms.ModelForm):
    class Meta:
        model = ChartOfAccount
        fields = '__all__'