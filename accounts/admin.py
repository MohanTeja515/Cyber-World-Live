from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomAbstractUser

class CustomAbstractUserAdmin(UserAdmin):
    model = CustomAbstractUser

    fieldsets = UserAdmin.fieldsets + (
            # (None, {'fields': ('some_extra_data',)}),
    )

admin.site.register(CustomAbstractUser, CustomAbstractUserAdmin)
