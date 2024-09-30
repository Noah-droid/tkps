from django import forms
from .models import Errand, RentalItem

class ErrandForm(forms.ModelForm):
    class Meta:
        model = Errand
        fields = ['errand_type', 'description']



class RentalForm(forms.Form):
    item = forms.ModelChoiceField(queryset=RentalItem.objects.filter(is_available=True))
