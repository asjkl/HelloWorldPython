from django.http import HttpResponse

# qui andiamo a definire le viste, cioe cosa andiamo a visualizzare

def benvenuto(request):
    return HttpResponse("Hello World")



