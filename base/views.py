from itertools import product
from django.http import JsonResponse
from .models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view



# Create your views here.
@api_view(['GET','POST'])
def index(request):
        return JsonResponse({'test':'test'})


# desc,   price,  prodName,     createdTime,    _id 
@api_view(['GET','POST'])
def products(request, id=-1):

             
    if request.method == 'GET':
        if int(id) > int(-1):
            product = Product.objects.all()[int(id)]
            return JsonResponse({
                "desc":product.desc,
                "price":product.price,
                "prodName":product.prodName,
                "createdTime":product.createdTime.date(),
              },safe=False)
     



        # get all
        res=[] # create an empty list
        for productObj in Product.objects.all():  # run on every row in the table...
            res.append({
                "desc" : productObj.desc,
                "price" : productObj.price,
                "prodName" : productObj.prodName,
                "createdTime" : productObj.createdTime,
                "_id" : productObj._id,
                })  # applend row by to row to res list
        return JsonResponse({'test':'GET'})
        # return JsonResponse(res, safe=False) # returen an array as json respinse


    if request.method == 'POST':

        print(request.data['name'])
        return JsonResponse({"res":"test"}, safe=False) # returen an array as json respinse




