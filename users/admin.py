#!/usr/bin/env python

##Third party imports
from django.contrib import admin

#Local application imports
from .models import User


class UserAdmin(admin.ModelAdmin):
    search_fields=("username",)
    ordering = ["first_name"]
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
admin.site.register(User, UserAdmin)