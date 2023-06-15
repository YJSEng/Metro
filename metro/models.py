from django.db import models
from phone_field import PhoneField

# Create your models here.


class Member(models.Model):
  firstname = models.CharField(max_length=9,blank=False,null=False)
  lastname = models.CharField(max_length=20)
  card=models.CharField(max_length=3,default="Yes")
  topup=models.IntegerField(default=100)
  phonenumber = models.CharField(max_length=12, unique=True, error_messages={
      "unique": "The Adhar Number exits."
  })
