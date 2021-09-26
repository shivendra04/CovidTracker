from django.shortcuts import render
from USER.forms import Userform,AssesmentForm
from USER.models import registerUser,SelfAssessment

# Create your views here.
def index_view(request):
    return render(request,'Index/index.html')

def add_user_detail(request):
    form = Userform()
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
        return index_view()
    return render(request,'USER/register.html',{'form':form})

def self_assement(request):
    form = AssesmentForm()
    if request.method == 'POST':
        risk = dict()
        form = AssesmentForm(request.POST)
        if form.is_valid():
            if form.travelHistory == False and form.contactWithCovidPatient == False and symptoms not in ["fever","cold","cough"]:
                risk['riskPercentage'] = '5%'
            elif form.travelHistory == True and form.contactWithCovidPatient == False and symptoms not in ["fever","cold","cough"]:
                risk['riskPercentage'] = '50%'
            elif form.travelHistory == False and form.contactWithCovidPatient == True and symptoms not in ["fever","cold","cough"]:
                risk['riskPercentage'] = '50%'
            elif form.travelHistory == False and form.contactWithCovidPatient == False and symptoms in ["fever","cold","cough"]:
                risk['riskPercentage'] = '50%'
            elif form.travelHistory == False and form.contactWithCovidPatient == True and symptoms in ["fever","cold","cough"]:
                risk['riskPercentage'] = '75%'
            elif form.travelHistory == True and form.contactWithCovidPatient == False and symptoms in ["fever","cold","cough"]:
                risk['riskPercentage'] = '75%'
            elif form.travelHistory == True and form.contactWithCovidPatient == True and symptoms not in ["fever","cold","cough"]:
                risk['riskPercentage'] = '75%'
            else:
                risk['riskPercentage'] = '95%'
            return render(request,'USER/rist_result.html',{'risk':risk})
