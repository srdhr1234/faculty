# Generated by Django 3.0.4 on 2021-09-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210912_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='form_submitted',
            field=models.BooleanField(default=False),
        ),
    ]