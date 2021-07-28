from django.contrib import admin
from tasks.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'addressee', 'send_datetime',
                    'closed')
