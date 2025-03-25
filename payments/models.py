from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    status_choice = [
        ("Pending","Pending"),
        ("Successful","SuccessFul"),
        ("Failed","Failed"),
        ("Refund","Refund"),
    ]
    
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=200,unique=True)
    payment_id = models.CharField(unique=True,blank=True,max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=status_choice, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Payment {self.order_id} - {self.status}"