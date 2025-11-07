from django.http import JsonResponse

def HelloViews(request):
    print(request.headers)
    print(request.method)
    return JsonResponse({"Hello":"World"})


def HelloWorld(request, username):
    print(username)
    return JsonResponse({"Hello":username})
