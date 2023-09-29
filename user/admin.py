from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Athlete, Sponsor
class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','is_staff')
    search_fields = ('username','email',)
    list_filter = ('is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password1','password2', 'email','phone_number', 'is_staff', 'is_active', 'role', 'groups', 'user_permissions'),
        }),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Athlete)
admin.site.register(Sponsor)