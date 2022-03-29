import django_filters
from django import forms

from django_filters import DateFilter
from .models import *
from django.contrib.auth.models import User



class DetailsFilter(django_filters.FilterSet):
        dep = (('CMPN','CMPN'),('IT','IT'))
        initial_date = django_filters.DateFromToRangeFilter(field_name="start_date",label="Date Range",lookup_expr="gte",widget=django_filters.widgets.RangeWidget(attrs={'type':'date'}))
        durations = django_filters.RangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'size':2}))
        department = django_filters.ChoiceFilter(choices=dep)
        faculty__first_name = django_filters.CharFilter(label="Faculty Name",lookup_expr='icontains')
        
        class Meta:
                model = Details
                fields = ['department','faculty__first_name','academic_years','typeas','events','durations']

class DetailsFilter_hod(django_filters.FilterSet):
              
        faculty__first_name = django_filters.CharFilter(label="Faculty Name",lookup_expr='icontains')
        initial_date = django_filters.DateFromToRangeFilter(field_name="start_date",label="Date Range",lookup_expr="gte",widget=django_filters.widgets.RangeWidget(attrs={'type':'date'}))
        durations = django_filters.RangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'size':2}))
        
        
        class Meta:
                model = Details
                fields = ['faculty__first_name','academic_years','typeas','events','durations']
             
class DetailsFilter_indi(django_filters.FilterSet):

        class Meta:
                model = Details
                fields = ['academic_years','typeas','events']
       
class ProjectCompFilter(django_filters.FilterSet):

        class Meta:
                model = ProjectComp
                fields = ['academic_years']

class ResearchGrantFilter(django_filters.FilterSet):

        class Meta:
                model = ResearchGrant
                fields = ['academic_years']

class AcademicRRFilter(django_filters.FilterSet):

        class Meta:
                model = AcademicRR
                fields = ['academic_years']

class PublicationAwardFilter(django_filters.FilterSet):

        class Meta:
                model = PublicationAward
                fields = ['academic_years']

class ConsultancyFilter(django_filters.FilterSet):

        class Meta:
                model = Consultancy
                fields = ['academic_years']

class ExpertLectureFilter(django_filters.FilterSet):

        class Meta:
                model = ExpertLecture
                fields = ['academic_years','years']