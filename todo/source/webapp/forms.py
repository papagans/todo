from django import forms
from django.forms import widgets
from webapp.models import status_choices


class TodoForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    details = forms.CharField(max_length=3000, required=True, label='Details', widget=widgets.Textarea)
    status = forms.ChoiceField(required=False, label='Status', initial="New", choices=status_choices)
    date = forms.DateField(required=False, label='Date', widget=widgets.SelectDateWidget)
