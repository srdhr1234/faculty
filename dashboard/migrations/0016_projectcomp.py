# Generated by Django 3.0.4 on 2021-09-18 10:21

import dashboard.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0015_auto_20210915_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotype', models.CharField(choices=[('National', 'National'), ('International', 'International')], default='', max_length=20)),
                ('event_type', models.CharField(choices=[('SIH', 'SIH'), ('Avishkar', 'Avishkar'), ('Others', 'Others')], default='', max_length=20)),
                ('others', models.CharField(blank=True, default='', max_length=100, verbose_name='')),
                ('award', models.CharField(choices=[('Prize Money', 'Prize Money'), ('Intership', 'Intership'), ('Certificate', 'Certificate')], default='', max_length=20)),
                ('Proof', models.FileField(blank=True, default='', upload_to=dashboard.models.get_upload_competition, verbose_name='Proof (only PDF)')),
                ('faculty', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
