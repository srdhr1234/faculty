from django import forms
from .models import Publication_C,Publication_J,BookChapter,Book,Patent,Copyright
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type='date'
    
class Publication_CForm(forms.ModelForm):

    class Meta:
        model = Publication_C
        fields = ['academic_years','title','cname','authname','pubyears','indexs','scopus','scopus_value', 'pagef', 'paget', 'doi','issn','publisher','certificate']

class Publication_JForm(forms.ModelForm):
    class Meta:
        model = Publication_J
        fields = ['academic_years','title','jname','authname', 'indexs', 'ctypes','scopus','scopus_value', 'volno','issueno','pageno','pubyears','doi','publisher','certificate']

class BookChapterForm(forms.ModelForm):

    class Meta:
        model = BookChapter
        fields = ['academic_years','chapter_title','book_name','editors','volno','issueno','pageno','pubyears','doi','publisher','certificate']


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['academic_years','book_name','authname','publisher','isbn','doi','pubyears','certificate']

class PatentForm(forms.ModelForm):

    class Meta:
        model = Patent
        fields = ['academic_years','title','ptype','patentno','grantyears','issueauth', 'issuec','term','certificate']


class CopyrightForm(forms.ModelForm):

    class Meta:
        model = Copyright
        fields = ['academic_years','title','grantdate','regno','issueauth', 'issuec','certificate']
        widgets = {
        'grantdate': DateInput(),
    }