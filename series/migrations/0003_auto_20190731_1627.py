import os
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('series', '0002_ethnics'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_DB_NAME = "series"

        superuser = User.objects.create_superuser(
            username="admin",
            email="xnazgul@gmail.com",
            password="1qazXSW.")
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
