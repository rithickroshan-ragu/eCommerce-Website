from django.http import JsonResponse
from products.models import Product

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
