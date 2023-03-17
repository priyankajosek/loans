from django.db import models
# Create your models here.


class Loan(models.Model):
    loan_amount = models.FloatField()
    interest = models.FloatField()
    tenure = models.IntegerField()
    type = models.CharField(max_length=255,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)