from django import forms

class TicketForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    name.widget.attrs['class'] = 'form-control'
    name.widget.attrs['placeholder'] = 'Full name'
    
    num_of_tickets = forms.IntegerField(label="NumOfTickets", min_value=1, max_value=100)
    num_of_tickets.widget.attrs['class'] = 'form-control'
    num_of_tickets.widget.attrs['placeholder'] = 'No. of tickets'
    
    choice_list = [("", "Ticket Type"), ("Regular", "Regular - 2500/-"), ("Platinum", "Platinum - 3500/-"), ("VIP", "VIP - 10000/-")]
    ticket_type = forms.ChoiceField(label="TicketType", choices=choice_list)
    ticket_type.widget.attrs['class'] = 'form-control'
