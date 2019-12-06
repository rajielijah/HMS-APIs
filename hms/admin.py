from django.contrib import admin
from .models import *

class HostelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'gender', 'no_of_block', 'warden'
    ]
admin.site.register(Hostel, HostelAdmin)

class BlockAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'hostel'
    ]
admin.site.register(Block, BlockAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = [
        'no', 'block', 'condition'
    ]
admin.site.register(Room, RoomAdmin)

class WardenAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'staff_id', 'gender'

    ]
admin.site.register(Warden, WardenAdmin)