from django.contrib import admin
from .models import ServiceRequest

admin.site.site_header = "Admin Portal"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin Portal"


class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status',)
    search_fields = ('customer__username', 'request_type')

admin.site.register(ServiceRequest, ServiceRequestAdmin)
