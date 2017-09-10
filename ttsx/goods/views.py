from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'goods/index.htm.html')

def list(request):
    value=request.POST.get('s1')

