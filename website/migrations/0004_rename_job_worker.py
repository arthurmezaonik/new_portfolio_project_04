# Generated by Django 3.2 on 2021-12-29 21:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0003_remove_review_approved'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Worker',
        ),
    ]
