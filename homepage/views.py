from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
# from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

from homepage.models import Ticket
from homepage.forms import TicketForm


def index(request):
    html = "index.html"
    my_ticket = Ticket.objects.all()
    return render(request, html, {'New': my_ticket, "welcome_name": 'Box'})


def ticket_detail_view(request, ticket_id):
    html = 'new_ticket_detail.html'
    ticket_detail = Ticket.objects.filter(id=ticket_id).first()
    return render(request, html, {'ticket': ticket_detail})




