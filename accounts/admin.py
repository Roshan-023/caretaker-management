from django.contrib import admin
from .models import UserAccount

@admin.register(UserAccount)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')