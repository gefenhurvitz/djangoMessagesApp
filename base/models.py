from django.db import models
from django.contrib.auth.models import User
 
 
class Product(models.Model):
    # user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    prodName = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
    fields =['_id','desc','price']

    def __str__(self):
     	   return f'{self.desc} : {self.prodName}'



class Message(models.Model):
    sender =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # receiver =models.ForeignKey(User,on_delete=models.SET_NULL)
    subject = models.CharField(max_length=50,null=True,blank=True)
    message = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	   return f'sub:{self.subject} from: {self.sender}'




class Note(models.Model):
    body = models.TextField(null = True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.body[0:50]