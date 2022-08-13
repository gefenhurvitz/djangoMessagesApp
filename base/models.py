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