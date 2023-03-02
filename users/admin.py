from django.contrib import admin
from users.models import Account, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class StudentIDInline(admin.StackedInline):
     model = Account
     can_delete = False
     verbose_name_plural = 'Users'

class CustomizedUserAdmin(UserAdmin):
    inlines = (StudentIDInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Account)

#Profile model registration
admin.site.register(Profile)