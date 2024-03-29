# Generated by Django 3.0.4 on 2021-09-15 05:42

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20210913_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='aadharproof',
            field=models.FileField(default='', upload_to=dashboard.models.get_upload_profile, verbose_name='PanAadhar Card (only PDF)'),
        ),
        migrations.AddField(
            model_name='myprofile',
            name='panproof',
            field=models.FileField(default='', upload_to=dashboard.models.get_upload_profile, verbose_name='Pan Card (only PDF)'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='edbe',
            field=models.FileField(default='', upload_to=dashboard.models.get_upload_profile, verbose_name='B.E. Certificate (only PDF)'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='edme',
            field=models.FileField(default='', upload_to=dashboard.models.get_upload_profile, verbose_name='M.E. Certificate (only PDF)'),
        ),
    ]
