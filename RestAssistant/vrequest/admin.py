from django.contrib import admin
from .models import Category

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("name","category_image")
    prepopulated_fields = {"slug":("name", "category_image")}

admin.site.register(Category,MemberAdmin)

