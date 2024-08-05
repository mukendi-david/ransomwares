from django.contrib import admin
from .models import TrafficCapture, EmailFilter, BackupData

admin.site.register(TrafficCapture)
admin.site.register(EmailFilter)
admin.site.register(BackupData)
