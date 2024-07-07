from django.contrib import admin

from . models import Task

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'is_completed', 'updated_date', 'created_date')


admin.site.register(Task,BookingAdmin)



