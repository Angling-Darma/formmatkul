from django.shortcuts import render
from django.http import HttpResponse
from form.models import Matkul

# Create your views here.
def fungsi_formulir(request):
    response={}
    return render(request,'form.html',response)

def fungsi_hasil(request):
    if request.method == 'POST':
       Matkul.objects.create(nama=request.POST['nama'],desc=request.POST['desc']) 
    all_matkul = Matkul.objects.all()
    response={'all_matkul':all_matkul}
    return render(request,'hasil.html',response)