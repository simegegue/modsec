from django import forms
from models import Rule,Log,Path

class selectRule(forms.Form):
    ruleSel=forms.ModelChoiceField(queryset=Rule.objects.all(),label="Elige una regla a buscar")
    
class selectLog(forms.Form):
    logSel=forms.ModelChoiceField(queryset=Log.objects.order_by('-dCreation'),label="Elige un registro a buscar")
    
class ruleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields=('text', )
        exclude=['lastMod','name']
 
class createRuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields=('name', 'text','path' )
        exclude=['lastMod']
               
class pathForm(forms.ModelForm):
    class Meta:
        model = Path
        fields=('text', )
