from django.shortcuts import render

# Create your views here.


def data_drive_home(request):
    return render(request, 'datadrive/index.html')