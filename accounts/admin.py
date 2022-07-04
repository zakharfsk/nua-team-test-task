from django.contrib import admin
from .models import UserModel

# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_id', 'first_name', 'last_name', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('username', 'user_id', 'first_name', 'last_name', 'user_json')
    ordering = ('-created_at',)


admin.site.register(UserModel, UserModelAdmin)
