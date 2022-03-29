from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','dept')
    ordering = ['dept']

admin.site.register(Details)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Show_Achieve)
admin.site.register(MyProfile)
admin.site.register(ProjectComp)
admin.site.register(ResearchGrant)
admin.site.register(AcademicRR)
admin.site.register(PublicationAward)
admin.site.register(Consultancy)
admin.site.register(ExpertLecture)



