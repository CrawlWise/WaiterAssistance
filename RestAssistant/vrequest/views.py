from django.shortcuts import render
from .models import Category  # This automatically import my model category to the view


# Create your views here.
def vrequest(request):
    # import categories from admin
    category_model = Category.objects.all().values()
    categoryValues = {
        "myCategoryData": category_model,
    }
    return render(request, 'request.html', categoryValues)
