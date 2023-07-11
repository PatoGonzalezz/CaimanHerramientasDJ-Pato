from .models import Tipo
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass

class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = ["tipo",]
        labels = {"tipo":"Tipo",}

