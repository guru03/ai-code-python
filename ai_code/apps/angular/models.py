from django.utils import timezone

from django.db import models

from common_models.status_choices import STATUS_CHOICES


class Angular(models.Model):

    id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100, default="01", unique=True)
    category = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, default="general")
    content_status = models.CharField(choices=STATUS_CHOICES, default="pending")
    visible = models.BooleanField(default=True)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    answer2 = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    angular_questions = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.question[:50]

    class Meta:
        db_table = "apps_angular"
