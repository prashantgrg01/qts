from django.db import models

# Create your models here.
class TicketRecord(models.Model):
    name = models.CharField(max_length=100)
    ticket_type = models.CharField(max_length=30)
    entrants = models.IntegerField()
    price = models.IntegerField()
    code_img = models.ImageField(default=None)

    def __str__(self):
        return self.name