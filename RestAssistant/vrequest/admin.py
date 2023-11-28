from django.contrib import admin
from .models import Category, ShowAllFood
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("name","category_image")
    prepopulated_fields = {"slug":("name", "category_image")}

admin.site.register(Category,MemberAdmin)

# Registering the showAllFood Category to the admin portal
class ShowAllFoodDisplay(admin.ModelAdmin):
    list_display = ("name", "foodImage", "description", "price")
    prepopulated_fields = {"slug":("name",)} # Slug must be a tuple

admin.site.register(ShowAllFood, ShowAllFoodDisplay)

