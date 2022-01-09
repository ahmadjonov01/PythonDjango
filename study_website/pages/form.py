from django import forms
from .models import natijalar

class NatijaForm(forms.ModelForm):
    class Meta:
        model = natijalar
        fields = "__all__"
