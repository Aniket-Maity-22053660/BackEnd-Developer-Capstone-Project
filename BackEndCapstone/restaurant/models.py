from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=12, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.Name