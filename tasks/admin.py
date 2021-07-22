from django.contrib import admin
from tasks.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender_id', 'addressee_id', 'send_datetime',
                    'closed')
