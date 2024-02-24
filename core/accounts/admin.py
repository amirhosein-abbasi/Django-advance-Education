from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile



class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','is_active','is_superuser','is_active',)
    list_filter = list_display
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication Dayi jan', {
            "fields":(
                'email','password'
            ),
        }),
         ('Permissions Dayi jan', {
            "fields":(
                'is_staff','is_active', 'is_superuser'
            ),
        }),
          ('Group Permissions Dayi jan', {
            "fields":(
                'groups', 'user_permissions'
            ),
        }),
          ('Important dates Dayi jan', {
            "fields":(
                'last_login',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields':('email','password1','password2','is_staff','is_active','is_superuser')
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
