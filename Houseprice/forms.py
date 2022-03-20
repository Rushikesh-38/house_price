from django import forms
from .models import Modelfeedback
class Queryform (forms.ModelForm):
    class Meta:
        model = Modelfeedback
        fields = '__all__'

