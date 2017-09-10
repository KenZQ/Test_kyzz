from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'goods/index.html')

# def list(request):
#     value=request.POST.get('s1')
def model01(request):
    return render(request, 'goods/model01.html')
def model02(request):
    return render(request, 'goods/model02.html')
def model03(request):
    return render(request, 'goods/model03.html')
def model04(request):
    return render(request, 'goods/model04.html')
def model05(request):
    return render(request, 'goods/model05.html')
def model06(request):
    return render(request, 'goods/model06.html')