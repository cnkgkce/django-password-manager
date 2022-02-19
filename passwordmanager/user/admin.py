from django.contrib import admin
from .models import Password


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('key','password','username')




admin.site.register(Password,UserAdmin)