from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(Usuario)
class AdminUser(admin.ModelAdmin):
	pass