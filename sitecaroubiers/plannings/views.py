from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from plannings.models import Family
from plannings.forms import FamilyForm

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def gestion(request):
    families = Family.objects.all()
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            form = FamilyForm()
    else:
        form = FamilyForm()
    return render(request, 'pages/gestion.html', {'families':families, 'form':form})