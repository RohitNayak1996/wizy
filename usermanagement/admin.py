from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from usermanagement.forms import CustomUserCreationForm, CustomUserChangeForm
from usermanagement.models import CustomUser, Movies


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'is_staff', 'is_active','is_admin')
    list_filter = ('email', 'is_staff', 'is_active','is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_admin')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


# Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Movies)