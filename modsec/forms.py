from django import forms
from models import Rule,Log

class selectRule(forms.Form):
    ruleSel=forms.ModelChoiceField(queryset=Rule.objects.all(),label="Elige una regla a buscar")
    
class selectLog(forms.Form):
    logSel=forms.ModelChoiceField(queryset=Log.objects.all(),label="Elige un registro a buscar")