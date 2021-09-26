from django import forms
from Admin.models import registerAdmin
class Adminform(forms.ModelForm):
    class Meta:
        model = registerAdmin
        fields = '__all__'
