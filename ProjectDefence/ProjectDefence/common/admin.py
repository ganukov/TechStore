from django.contrib import admin

from ProjectDefence.common.models import Complaint


# Register your models here.
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    ordering = ('pk', 'first_name', 'subject')
    list_display = ['first_name', 'email', 'subject', 'message']
    list_filter = ('email', 'subject',)
    search_fields = ('pk', 'email', 'subject',)
    sortable_by = ('pk', 'email', 'subject',)
