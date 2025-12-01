from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the cuisine app!")

# Create your views here.
