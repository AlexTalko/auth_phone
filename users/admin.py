from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'first_name', 'last_name', 'ref_code', 'invite_code',)
    search_fields = ('phone', 'first_name', 'last_name', 'ref_code',)
    list_filter = ('id', 'phone', 'country', 'ref_code',)
