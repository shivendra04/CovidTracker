from django import forms
from USER.models import registerUser,SelfAssessment
class Userform(forms.ModelForm):
    class Meta:
        model = registerUser
        fields = '__all__'

class AssesmentForm(forms.ModelForm):
    class Meta:
        model = SelfAssessment
        fields = '__all__'
