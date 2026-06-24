from django.db import models
from common_enum.status import WorkStatus
from common_models.language_choice import LANGUAGE_CHOICES
from common_models.label_choice import LABEL_CHOICES
from common_models.code_language_choices import CODE_LANGUAGE_CHOICES


class Coding(models.Model):
    id = models.AutoField(primary_key=True)
    serial_number = models.IntegerField(unique=True)  # Angular expects number, not string

    language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES,
        default="angular"
    )

    difficulty = models.CharField(
        max_length=20,
        choices=LABEL_CHOICES,
        default="beginner"
    )

    topic = models.CharField(max_length=100, default="angular")

    visible = models.BooleanField(default=True)

    content_status = models.CharField(
        max_length=50,
        choices=[(status.value, status.name) for status in WorkStatus],
        default=WorkStatus.Draft.value,
    )

    programe = models.TextField(blank=True, null=True)  # maps to Angular `programe`
    solution = models.TextField(blank=True, null=True)   # maps to Angular `soution`
    alternate_solution = models.TextField(blank=True, null=True)  # optional

    code_language = models.CharField(
        max_length=50,
        choices=CODE_LANGUAGE_CHOICES,
        default="typescript"
    )
    code_block_title = models.CharField(max_length=100, blank=True, null=True)
    code_editor = models.TextField(blank=True, null=True)  # maps to Angular `code_editor`

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.language} - {self.topic}"

    class Meta:
        db_table = "apps_coding"
