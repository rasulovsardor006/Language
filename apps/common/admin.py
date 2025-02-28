from django.contrib import admin
from django.utils.html import mark_safe
from apps.common.models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'ico_code', 'flag')

    @admin.display(description='Flag')
    def flag(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" width="20" height="20" alt="{obj.name}" />')
        return "-"
