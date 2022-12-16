from django.contrib import admin

from ProjectDefence.common.models import Complaint


# Register your models here.
@admin.register(Complaint)
class OrderItemAdmin(admin.ModelAdmin):
    pass
