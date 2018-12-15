from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["itemV","priority","completed"]
        
        
        
class FilterForm(forms.Form):
    priority = forms.IntegerField()
    do_status = forms.BooleanField(label='Is done?')