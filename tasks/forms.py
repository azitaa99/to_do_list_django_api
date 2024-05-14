
from django  import forms
from .models import Task

class taskcreateform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','complite']
