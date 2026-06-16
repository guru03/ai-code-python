from django.utils import timezone

from django.db import models

from common_models.label_choice import LABEL_CHOICES
from common_models.language_choice import LANGUAGE_CHOICES
from common_enum.status import WorkStatus
# from common_models.status_choices import STATUS, STATUS_CHOICES


class Angular(models.Model):

    id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100, default="01", unique=True)

    language = models.CharField(
        max_length=50, choices=LANGUAGE_CHOICES, default="angular"
        # max_length=50, 
        # choices=[(status.value, status.name) for status in WorkStatus],
        # default="angular"
    )
    
    label = models.CharField(
        max_length=20,
        choices=LABEL_CHOICES,
        default="beginner"
    )

    topic = models.CharField(max_length=100, default="angular")

    # Add content_status with choices
    # status = models.CharField(
    #     max_length=20,
    #     choices=STATUS,
    #     default="draft"
    # )

    content_status = models.CharField(
        max_length=50,
        choices=[(status.value, status.name) for status in WorkStatus],
        default=WorkStatus.Draft.value,
    )
    visible = models.BooleanField(default=True)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    answer2 = models.TextField(blank=True, null=True)
    code_block = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    angular_questions = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.question[:50]

    class Meta:
        db_table = "apps_angular"
