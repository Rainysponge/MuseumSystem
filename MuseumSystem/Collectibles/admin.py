from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoryName')


@admin.register(collectible)
class collectibleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'time')


@admin.register(love)
class loveAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'collectible')


@admin.register(device)
class deviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'collectible', 'deviceId')


@admin.register(light)
class lightAdmin(admin.ModelAdmin):
    list_display = ('id', 'collectible', 'lightID')


@admin.register(monitorLimit)
class monitorLimitAdmin(admin.ModelAdmin):
    list_display = ('id', 'collectible')
