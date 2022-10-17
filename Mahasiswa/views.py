from django.shortcuts import render, redirect
from matplotlib.style import context
from requests import request
from .forms import MahasiswaForm
from .models import Mahasiswa

# Create your views here.
def create_mahasiswa(request):
    if request.method == "POST":
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = MahasiswaForm()
    return render(request, 'create.html',{'form':form})


def retrieve_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request,'search.html',{'mahasiswas':mahasiswas})


def update_mahasiswa(request,pk):
    mahasiswas = Mahasiswa.objects.get(id=pk)
    form = MahasiswaForm(instance=mahasiswas)

    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mahasiswas)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'mahasiswas':mahasiswas,
        'form':form,
    }
    return render(request,'update.html',context)


def delete_mahasiswa(request,pk):
    mahasiswas = Mahasiswa.objects.get(id=pk)

    if request.method == 'POST':
        mahasiswas.delete()
        return redirect('/')

    context = {
        'mahasiswas':mahasiswas,
    }
    return render(request,'remove.html',context)
