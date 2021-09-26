from django.shortcuts import render
from Admin.forms import Adminform
from Admin.models import registerAdmin

# Create your views here.
def index_view(request):
    return render(request,'Index/index.html')

def add_admin_detail(request):
    form = Adminform()
    if request.method == 'POST':
        form = Adminform(request.POST)
        if form.is_valid():
            form.save()
        return index_view()
    return render(request,'Admin/register.html',{'form':form})
def update_covid_result(request):
    pass
