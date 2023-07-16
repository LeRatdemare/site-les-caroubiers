from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from plannings.models import Family

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def gestion(request):
    families = Family.objects.all()
    return render(request, 'pages/gestion.html', {'families' : families})