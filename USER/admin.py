from django.contrib import admin
from USER.models import registerUser
# Register your models here.
class RegisterUserAdmin(admin.ModelAdmin):
    list_display = ['name','phoneNumber','pinCode']

admin.site.register(registerUser,RegisterUserAdmin)
