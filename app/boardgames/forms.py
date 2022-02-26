from datetime import date
from xml.dom import ValidationErr

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField, ValidationError
from django.core.exceptions import ValidationError

from .models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
        }