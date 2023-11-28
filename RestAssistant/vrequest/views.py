from django.shortcuts import render
from .models import Category, ShowAllFood  # This automatically import my model category to the view


# Create your views here.
def vrequest(request):
    # import categories from admin
    category_model = Category.objects.all().values()
    # Import the showAllFood module to my view
    showAllFoodModel = ShowAllFood.objects.all().values()
    categoryValues = {
        "myCategoryData": category_model,
        "showAllFoodCategory": showAllFoodModel,
    }
    return render(request, 'request.html', categoryValues)
