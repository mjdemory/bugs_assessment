from django import forms
from homepage.models import Ticket


class TicketForm(forms.Form):
    title = forms.CharField(max_length=80)
    description = forms.TextField()
