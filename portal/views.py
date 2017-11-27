from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import TicketRecord
import pyqrcode
import os

# Create your views here.
def portal_page(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            return redirect('confirmation/')
    else:
        form = TicketForm()
    return render(request, "portal/portal_page.html", {"form": form})

def page_not_found(request):
    return render(request, "404.html")

# Global id variable
num_id = 101

def confirmation(request):
    if request.method == "GET":
        return redirect("/page_not_found/")
    
    global num_id
    name = request.POST.get("name", "")
    num_of_tickets = request.POST.get("num_of_tickets", "")
    ticket_type = request.POST.get("ticket_type", "")
    token = request.POST.get("stripeToken", "")

    if ticket_type == "Regular":
        price = int(num_of_tickets) * 2500
    elif ticket_type == "Platinum":
        price = int(num_of_tickets) * 3500
    else:
        price = int(num_of_tickets) * 10000

    ticket = TicketRecord()
    ticket.name = name
    ticket.ticket_type = ticket_type
    ticket.entrants = num_of_tickets
    ticket.price = price
    ticket.id = num_id
    num_id += 1
    
    data = "Paradox City Inc\nEvent Name - Sanam's Concert\nTicket Id - "+str(ticket.id)+"\nEntrants - "+str(ticket.entrants)
    path = "portal/static/portal/images/"
    image = "qr"+str(ticket.id)+".png"; 
    code = pyqrcode.create(data)
    code.png(path+image, scale=6)
    ticket.code_img = "static/portal/images/"+image
    ticket.save()

    return render(request, "portal/confirmation.html", {"ticket": ticket, "token": token})