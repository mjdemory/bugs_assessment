from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_user.models import MyUser

# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Custom Fields',
#             {
#                 'fields': (
#                     'age',
#                     'displayname',
#                     'homepage',
#                 )
#             }
#         )
#     )


admin.site.register(MyUser, UserAdmin)