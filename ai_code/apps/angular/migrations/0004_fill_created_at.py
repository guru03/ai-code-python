# apps/angular/migrations/0004_fill_created_at.py
from django.utils import timezone
from django.db import migrations


def set_created_at(apps, schema_editor):
    Angular = apps.get_model("angular", "Angular")
    Angular.objects.filter(created_at__isnull=True).update(created_at=timezone.now())
    Angular.objects.filter(updated_at__isnull=True).update(updated_at=timezone.now())


class Migration(migrations.Migration):
    dependencies = [
        ("angular", "0003_remove_angular_status_angular_updated_at_and_more"),
    ]
    operations = [
        migrations.RunPython(set_created_at),
    ]
