from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["itemV","priority","completed"]
        
        

### forms filter    
class FilterForm(forms.Form):
    priority = forms.IntegerField(min_value=0, max_value=5, initial=0)
    do_status = forms.NullBooleanField(label='Is done?')