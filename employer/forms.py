from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class EmployerRegisterForm(forms.Form):
    nom = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom",
                "class": "form-control"
            }
        ))
    prenom = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Prenom",
                "class": "form-control"
            }
        ))
    tel = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "tel",
                "class": "form-control"
            }
        ))
    tel_pro = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Tel_pro",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('nom', 'prenom', 'tel', 'tel_pro', )
