from django.contrib import admin
from .models import Sex, Profile


# Register your models here.
@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('id', 'sex')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'real_name', 'jurisdiction')
