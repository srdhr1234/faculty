# Generated by Django 3.0.4 on 2021-09-11 08:15

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_myprofile_totalm'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='apletter',
            field=models.FileField(default='', upload_to=dashboard.models.get_upload_profile, verbose_name='Resume (only PDF)'),
        ),
    ]
