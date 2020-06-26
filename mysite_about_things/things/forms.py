from datetime import date

from django.forms import ModelForm, DateInput, TimeInput
from django.core.exceptions import ValidationError

from .models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = '__all__'
       

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d >= date.today():
            raise ValidationError("you cannot bought stf in the future")
        return d