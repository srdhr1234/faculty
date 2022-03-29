from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
from django import forms
from django.core.validators import RegexValidator
from dashboard.models import Profile

# Create your models here.

def get_upload_path_conference(instance, filename):
    return 'publications/conference/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty, filename)

def get_upload_path_journal(instance, filename):
    return 'publications/journal/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty, filename)

def get_upload_path_bookchapter(instance, filename):
    return 'publications/bookchapter/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty, filename)

def get_upload_path_book(instance, filename):
    return 'publications/book/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty, filename)

def get_upload_path_patent(instance, filename):
    return 'publications/patent/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty, filename)

def get_upload_path_copyright(instance, filename):
    return 'publications/copyright/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty, filename)




class Publication_C(models.Model):
    department = models.CharField(max_length=50,default="")
    #FACULTY NAME
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    #academic_years=models.CharField(max_length=50,default="")
    #events=models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),      
    )
    academic_years=models.CharField(max_length=20,choices=academic_year,default="")

    title = models.CharField(verbose_name="Paper Title",max_length=300,default="")
    cname = models.CharField(verbose_name="Conference Name",max_length=300,default="")
    authname = models.CharField(verbose_name="Author Names",max_length=300,default="")
    

    pubyear=(
        ('2020','2020'),
        ('2021','2021'),   
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),   
    )
    pubyears=models.CharField(verbose_name="Year of publication",max_length=10,choices=pubyear,default="")

    index=(
        ('UGC','UGC'),
        ('SCI/SCIE','SCI/SCIE'),   
        ('ESCI','ESCI'),
        ('WOS','WOS'),
        ('Others','Others'),
    )
    indexs=models.CharField(verbose_name="Indexing",max_length=10,choices=index,default="")

    scopuss=(
        ('Yes','Yes'),
        ('No','No'),     
    )
    scopus=models.CharField(verbose_name="Is Scopus Index?",max_length=5,choices=scopuss,default="")
    scopus_value=models.CharField(verbose_name="Scopus Index Value",blank=True,max_length=5,default="",help_text='Scopus Index Value ')

    pagef = models.PositiveIntegerField(verbose_name="Pagef",default=0)

    paget = models.PositiveIntegerField(verbose_name="Pagest",default=0)

    doi = models.CharField(verbose_name="DOI",max_length=20,default="")

   
    issn = models.CharField(verbose_name="ISSN",max_length=50,default="")
    publisher = models.CharField(verbose_name="Publisher",max_length=50,default="")

    #CERTIFICATE
    certificate = models.FileField(verbose_name="Certificate (only PDF)",upload_to=get_upload_path_conference,blank=True,default="")

    #DATE THE DATA WAS ENTERED

    date_created = models.DateField(default =date.today)
    def __str__(self):
        return str(self.faculty)


class Publication_J(models.Model):
    department = models.CharField(max_length=50,default="")
    #FACULTY NAME
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    #academic_years=models.CharField(max_length=50,default="")
    #events=models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),       
    )
    academic_years=models.CharField(max_length=20,choices=academic_year,default="")

    title = models.CharField(verbose_name="Paper Title",max_length=300,default="")
    jname = models.CharField(verbose_name="Journal Name",max_length=300,default="")
    authname = models.CharField(verbose_name="Author Names",max_length=300,default="")

    index=(
        ('UGC','UGC'),
        ('SCI/SCIE','SCI/SCIE'),   
        ('ESCI','ESCI'),
        ('WOS','WOS'),
        ('Others','Others'),
    )
    indexs=models.CharField(verbose_name="Indexing",max_length=10,choices=index,default="")

    ctype=(
        ('Open Source','Open Source'),
        ('Free Journal','Free Journal'),   
        ('Paid','Paid'),
       
    )
    ctypes=models.CharField(verbose_name="Journal Type",max_length=20,choices=ctype,default="")

    scopuss=(
        ('Yes','Yes'),
        ('No','No'),     
    )
    scopus=models.CharField(verbose_name="Is Scopus Index?",max_length=5,choices=scopuss,default="")
    scopus_value=models.CharField(blank=True,max_length=5,default="")

    volno = models.PositiveIntegerField(verbose_name="Volume Number",default=1)

    issueno = models.PositiveIntegerField(verbose_name="Issue Number",default=1)

    pageno = models.CharField(verbose_name="Page(s)",max_length=10,default="")


    pubyear=(
        ('2020','2020'),
        ('2021','2021'),   
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),      
    )
    pubyears=models.CharField(verbose_name="Year of publication",max_length=10,choices=pubyear,default="")

    doi = models.CharField(verbose_name="DOI",max_length=50,default="")

    publisher = models.CharField(verbose_name="Publisher",max_length=50,default="")

     #CERTIFICATE
    certificate = models.FileField(verbose_name="Certificate (only PDF)",upload_to=get_upload_path_journal,blank=True,default="")

    #DATE THE DATA WAS ENTERED

    date_created = models.DateField(default =date.today)

    def __str__(self):
        return(self.faculty)

    
class BookChapter(models.Model):
    department = models.CharField(max_length=50,default="")
    #FACULTY NAME
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    #academic_years=models.CharField(max_length=50,default="")
    #events=models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),       
    )
    academic_years=models.CharField(verbose_name="Academic Year",max_length=10,choices=academic_year,default="")

    chapter_title=models.CharField(verbose_name="Chapter Title",max_length=300,default="")
    book_name=models.CharField(verbose_name="Book Name", max_length=300,default="")
    editors=models.CharField(verbose_name="Editors Name", max_length=300,default="")
    volno=models.PositiveIntegerField(verbose_name="Volume Number",default=1)
    issueno=models.PositiveIntegerField(verbose_name="Issue Number",default=1)
    pageno=models.CharField(verbose_name="Page(s)",max_length=50,default="")
    pubyear=(
        ('2020','2020'),
        ('2021','2021'),   
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),      
    )
    pubyears=models.CharField(verbose_name="Year of publication",max_length=10,choices=pubyear,default="")

    doi = models.CharField(verbose_name="DOI",max_length=50,default="")

    publisher = models.CharField(verbose_name="Publisher",max_length=50,default="")

    #CERTIFICATE
    certificate = models.FileField(verbose_name="Certificate (only PDF)",upload_to=get_upload_path_bookchapter,blank=True,default="")

    #DATE THE DATA WAS ENTERED

    date_created = models.DateField(default =date.today)

    def __str__(self):
        return(self.faculty)

class Book(models.Model):
    department = models.CharField(max_length=50,default="")
    #FACULTY NAME
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    #academic_years=models.CharField(max_length=50,default="")
    #events=models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),      
    )
    academic_years=models.CharField(verbose_name="Academic Year",max_length=20,choices=academic_year,default="")

    book_name=models.CharField(verbose_name="Book Name", max_length=300,default="")
    authname=models.CharField(verbose_name="Name of Authors", max_length=300,default="")
    publisher = models.CharField(verbose_name="Publisher",max_length=100,default="")
    isbn = models.CharField(verbose_name="ISBN",max_length=50,default="")
    doi = models.CharField(verbose_name="DOI",max_length=50,default="")
    
    pubyear=(
        ('2020','2020'),
        ('2021','2021'),   
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),      
    )
    pubyears=models.CharField(verbose_name="Year of publication",max_length=10,choices=pubyear,default="")
    
    #CERTIFICATE
    certificate = models.FileField(verbose_name="Certificate (only PDF)",upload_to=get_upload_path_book,blank=True,default="")

    #DATE THE DATA WAS ENTERED

    date_created = models.DateField(default =date.today)

    def __str__(self):
        return(self.faculty)

class Patent(models.Model):
    department = models.CharField(max_length=50,default="")
    #FACULTY NAME
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    #academic_years=models.CharField(max_length=50,default="")
    #events=models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),       
    )
    academic_years=models.CharField(verbose_name="Academic Year",max_length=10,choices=academic_year,default="")

    title=models.CharField(verbose_name="Patent Title", max_length=300,default="")
    ptype = models.CharField(verbose_name="Patent type",max_length=300,default="")
    patentno = models.PositiveIntegerField(verbose_name="Patent Number", default=0)
    grantyear=(
        ('2020','2020'),
        ('2021','2021'),   
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),      
    )
    grantyears = models.CharField(verbose_name="Grant Year",max_length=10,choices=grantyear,default="")

    issueauth = models.CharField(verbose_name="Issuing Authority",max_length=10,default="")
    issuec = models.CharField(verbose_name="Issuing Country",max_length=30,default="")

    term = models.PositiveIntegerField(verbose_name="Grant Term",default=0)

   #CERTIFICATE
    certificate = models.FileField(verbose_name="Certificate (only PDF)",upload_to=get_upload_path_patent,blank=True,default="")

    #DATE THE DATA WAS ENTERED

    date_created = models.DateField(default =date.today)

    def __str__(self):
        return(self.faculty)


class Copyright(models.Model):
    department = models.CharField(max_length=50,default="")
    #FACULTY NAME
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    #academic_years=models.CharField(max_length=50,default="")
    #events=models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),       
    )
    academic_years=models.CharField(verbose_name="Academic Year",max_length=20,choices=academic_year,default="")

    title=models.CharField(verbose_name="Copyright Title", max_length=300,default="")
   
    grantdate = models.DateField(verbose_name="Granted On",default =date.today)
    regno = models.CharField(verbose_name="Registration Number", max_length=100,default="")
    issueauth = models.CharField(verbose_name="Issuing Authority",max_length=10,default="")
    issuec = models.CharField(verbose_name="Issuing Country",max_length=30,default="")

   #CERTIFICATE
    certificate = models.FileField(verbose_name="Certificate (only PDF)",upload_to=get_upload_path_copyright,blank=True,default="")

    #DATE THE DATA WAS ENTERED

    date_created = models.DateField(default =date.today)

    def __str__(self):
        return(self.faculty)