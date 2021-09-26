from django.contrib import admin
from Admin.models import registerAdmin
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name','phoneNumber','pinCode']

admin.site.register(registerAdmin,RegisterAdmin)
