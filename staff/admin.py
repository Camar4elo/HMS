from django.contrib import admin
from staff.models import Rank, Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'rank',
                    'telegram_nickname', 'phone_number', 'personal_email',
                    'work_email', 'employment_date', 'date_of_birth')

    list_filter = ('rank', 'employment_date')


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ['rank']
