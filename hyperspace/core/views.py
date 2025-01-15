from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to H Y P E R S P A C E")