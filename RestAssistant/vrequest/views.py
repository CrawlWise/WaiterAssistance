from django.shortcuts import render

# Create your views here.
def vrequest(request):
    return render(request, 'index.html')
