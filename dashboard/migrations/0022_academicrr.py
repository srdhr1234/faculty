# Generated by Django 3.0.4 on 2021-09-18 18:10

import dashboard.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0021_researchgrant'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicRR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(default='', max_length=50)),
                ('academic_years', models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025')], default='', max_length=20, verbose_name='Academic Year')),
                ('syllabusset', models.CharField(choices=[('Syllabus Setting', 'Syllabus Setting'), ('BOS', 'BOS'), ('Moderator', 'Moderator'), ('Paper Setter', 'Paper Setter'), ('Reviewer for Journal', 'Reviewer for Journal'), ('Reviewer for Conference', 'Reviewer for Conference')], default='', max_length=30, verbose_name='Academic Year')),
                ('details', models.CharField(default='', max_length=100, verbose_name='Details of the role')),
                ('proof', models.FileField(blank=True, default='', upload_to=dashboard.models.get_upload_academicrr, verbose_name='Proof (only PDF)')),
                ('faculty', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
