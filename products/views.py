from django.http import JsonResponse
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.create_product_serializer import createProductSerializer


def HelloViews(request):
    print(request.headers)
    print(request.method)
    return JsonResponse({"Hello":"World"})


def HelloWorld(request, username):
    p = Product.objects.all()
    print(p)
    print(p[1])
    print(p[1].__dict__)
    print(p[1].name)

    return JsonResponse({"Hello":username})


@api_view(["POST"])
def createProduct(request):
    serializedData = createProductSerializer(data=request.data)    
    print(serializedData)
    if serializedData.is_valid():
        print(serializedData)
        # serialized data deos not have id
        prod = serializedData.save()
        # prod has product id (primary key)
        print("Product ID:", prod.id)

        # return JsonResponse({"Product ID:": prod.id})
        return Response(createProductSerializer(prod).data, status=status.HTTP_201_CREATED)


    return JsonResponse({"Error": serializedData.errors})
