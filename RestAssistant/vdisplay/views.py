from django.shortcuts import render

# Create your views here.
def vdisplay(request):
    return render(request, 'display.html')