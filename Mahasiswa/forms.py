from attr import fields
from django import forms
from django import forms
from django.forms import ModelForm
from matplotlib.pyplot import cla
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = "__all__"
