from django import forms
from ..models import Level

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['level_title', 'group', 'pre']  # Include both fields

    def clean(self):
        cleaned_data = super().clean()
        group = cleaned_data.get('group')
        pre = cleaned_data.get('pre')

        # Ensure that only one is provided
        if not group and not pre:
            raise forms.ValidationError("You must select either a group or a pre-level.")
        
        if group and pre:
            raise forms.ValidationError("You can select either a group or a pre-level, not both.")