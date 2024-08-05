from django.db import models
from django.contrib.auth.models import User


class TrafficCapture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_ip = models.CharField(max_length=100)
    destination_ip = models.CharField(max_length=100)
    protocol = models.CharField(max_length=20)
    length = models.IntegerField()
    info = models.TextField()
    captured_at = models.DateTimeField(auto_now_add=True)


class EmailFilter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    subject = models.TextField()
    content = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)


class BackupData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    backup_at = models.DateTimeField(auto_now_add=True)
