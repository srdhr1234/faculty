from django import forms
from .models import *
from django.contrib.auth.models import User



class DateInput(forms.DateInput):
    input_type='date'

class DataForm(forms.ModelForm):
   
    class Meta:
        model = Details
        fields = ['academic_years', 'typeas', 'modes', 'events','others', 'topic', 'college_name', 'start_date', 'end_date','certificate']
        
        widgets = {
        'start_date': DateInput(),
        'end_date': DateInput(),
    }

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['sal','dept']

class MyProfileForm(forms.ModelForm):

    class Meta:
        model = MyProfile
        fields = ['photo','dob','designation', 'doj', 'edbe','edme','edphd','expty','exptm', 'exptm', 'expiy','expim','pan', 'panproof', 'aadhar','aadharproof', 'resume','apletter']

        widgets = {
        'dob': DateInput(),
        'doj': DateInput(),
    }

class Show_AchieveForm(forms.ModelForm):

    class Meta:
        model = Show_Achieve
        fields = ['image']

class ProjectCompForm(forms.ModelForm):

    class Meta:
        model = ProjectComp
        fields = ['academic_years','cotype','event_type', 'others','award', 'proof']

class ResearchGrantForm(forms.ModelForm):

    class Meta:
        model = ResearchGrant
        fields = ['academic_years','title','amount','authority','term']

class AcademicRRForm(forms.ModelForm):

    class Meta:
        model = AcademicRR
        fields = ['academic_years','syllabusset','details','proof']

class PublicationAwardForm(forms.ModelForm):

    class Meta:
        model = PublicationAward
        fields = ['academic_years','type_pub','title','proof']

class ConsultancyForm(forms.ModelForm):

    class Meta:
        model = Consultancy
        fields = ['academic_years','type_con','orgdet','prodet','start_date','end_date','proof']

        widgets = {
        'start_date': DateInput(),
        'end_date': DateInput(),
    }

class ExpertLectureForm(forms.ModelForm):

    class Meta:
        model = ExpertLecture
        fields = ['academic_years','typeas','resource_person','subject','topic','years','date','present','attendance','proof']

        widgets = {
        'date': DateInput(),
    }



