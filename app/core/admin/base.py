from django.contrib import admin


class AdminBase(admin.ModelAdmin):
    """
    Base class for all admin classes in the application
    """
    readonly_fields = ('created_at', 'updated_at', 'id')
