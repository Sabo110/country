from django.forms import ModelForm
from .models import *

class ContinentForm(ModelForm):
    class Meta:
        model = Continent
        fields = ["name"]