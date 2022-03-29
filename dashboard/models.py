from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
from django import forms


# Create your models here.


def get_upload_path(instance, filename):
    return 'certificates/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty.username, filename)

def get_upload_profile(instance, filename):
    return 'profile/{0}/{1}'.format(instance.faculty.username, filename)

def get_upload_competition(instance, filename):
    return 'competition/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty.username, filename)

def get_upload_academicrr(instance, filename):
    return 'academicrr/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty.username, filename)

def get_upload_publicationaward(instance, filename):
    return 'publicationaward/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty.username, filename)

def get_upload_expert(instance, filename):
    return 'expert/{0}/{1}/{2}'.format(instance.academic_years,instance.faculty.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    sals=(
        ('Dr.','Dr.'),
        ('Mr.','Mr.'),
        ('Ms.','Ms.'),
        ('Mrs.','Mrs.'),       
                
    )
    sal=models.CharField(max_length=5,choices=sals,default="")

    depts=(        
        ('CMPN','CMPN'),        
        ('IT','IT'),
                        
    )
    dept=models.CharField(max_length=20,choices=depts)
    
    def __str__(self):
        return str(self.user)

class Details(models.Model):
   
    #DEPARTMENT NAME
    department = models.CharField(max_length=50,default="")
    #FACULTY NAME
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    
    #TYPE
    typea = (
        ('Attended','Attended'),
        ('Conducted','Conducted'),
    )
    typeas=models.CharField(verbose_name='Type',max_length=20,choices=typea,default="")

    mode = (
        ('Online','Online'),
        ('Offline','Offline'),
    )
    modes=models.CharField(verbose_name='Mode',max_length=20,choices=mode,default="")

    #ACADEMIC YEAR
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),     
    )
    academic_years=models.CharField(verbose_name='Academic Year',max_length=20,choices=academic_year,default="")

    
    # EVENT TYPE
    event=(
        ('STTP','STTP'),
        ('FDP','FDP'),
        ('Faculty Orienation Program','Faculty Orientation Program'),
        ('Webinar','Webinar'),
        ('NPTEL','NPTEL'),
        ('Udemy','Udemy'),
        ('Coursera','Coursera'),
        ('Others','Others'),
        
    )
    events=models.CharField(verbose_name='Event',max_length=50,choices=event,default="")

    others = models.CharField(verbose_name='',blank=True,max_length=100,default="")

    # Title of STTP/FDP/Webinar/NPTEL/Coursera
    topic = models.CharField(verbose_name='Topic',max_length=100,default="")

    #College Name (if Coursera, then write Online)
    college_name = models.CharField(verbose_name='College Name',max_length=100,default="")
    
    #START DATE
    start_date = models.DateField(verbose_name='Start Date', default =date.today)

    #END DATE
    end_date = models.DateField(verbose_name='End Date', default =date.today)
 
    durations=models.IntegerField(default=0)
    
    #CERTIFICATE
    certificate = models.FileField(verbose_name="Certificate (only PDF)",upload_to=get_upload_path,blank=True,default="")

    #DATE THE DATA WAS ENTERED
    date_created = models.DateField(default =date.today)        

    @property
    def cal_duration(self):
        
        durations = (self.end_date - self.start_date).days
        durations = durations+1
        return durations
    def save(self, *args, **kwarg):
        self.durations = self.cal_duration
        
        super(Details, self).save(*args, **kwarg)

    def __str__(self):
        return str(self.faculty)
    
class Show_Achieve(models.Model):
    is_active=models.BooleanField(default=False)    
    image = models.ImageField(upload_to='images/',blank=True,default="")
    date_uploaded = models.DateField(default =date.today)

    def __str__(self):
        return str(self.date_uploaded)


    
class MyProfile(models.Model):

    form_submitted = models.BooleanField(default=False)


    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    
    photo = models.ImageField(verbose_name="Image", upload_to=get_upload_profile,default=None)
    dob = models.DateField(verbose_name='Date of Birth', default =date.today)

    designations=(
        ('Professor','Professor'),
        ('Associate Professor','Associate Professor'),
        ('Assistant Professor','Assistant Professor'),     
                
    )
    designation = models.CharField(max_length=20,choices=designations,default="")
    doj = models.DateField(verbose_name='Date of Joining', default =date.today)

    edbe = models.FileField(verbose_name="B.E. Certificate (only PDF)",upload_to=get_upload_profile,default="")

    edme = models.FileField(verbose_name="M.E. Certificate (only PDF)",upload_to=get_upload_profile,default="")

    edphd = models.FileField(verbose_name="Phd. Certificate (only PDF)",upload_to=get_upload_profile,blank=True,default="")

    pan = models.CharField(verbose_name='PAN Card Number',max_length=20,default="")
    panproof = models.FileField(verbose_name="Pan Card (only PDF)",upload_to=get_upload_profile,default="")

    aadhar = models.CharField(verbose_name='Aadhar Card Number',max_length=20,default="")
    aadharproof = models.FileField(verbose_name="PanAadhar Card (only PDF)",upload_to=get_upload_profile,default="")

    expty = models.PositiveIntegerField(verbose_name="Teaching Experience in years",default=0)
    exptm = models.PositiveIntegerField(verbose_name="Teaching Experience in months",default=0)

    expiy = models.PositiveIntegerField(verbose_name="Industry Experience in years",default=0)
    expim = models.PositiveIntegerField(verbose_name="Industry Experience in months",default=0)

    totaly = models.IntegerField(default=0)
    totalm = models.IntegerField(default=0)

    resume = models.FileField(verbose_name="Resume (only PDF)",upload_to=get_upload_profile,default="")
    apletter = models.FileField(verbose_name="Appointment Letter (only PDF)",upload_to=get_upload_profile,default="")

    @property
    def cal_expy(self):        
        yrs = (self.expty + self.expiy)       
        return yrs
    def save(self, *args, **kwarg):
        self.totaly = self.cal_expy       
        super(MyProfile, self).save(*args, **kwarg)
    @property
    def cal_expm(self):       
        months = (self.exptm + self.expim)
        return months
    def save(self, *args, **kwarg):  
        self.totalm = self.cal_expm
        super(MyProfile, self).save(*args, **kwarg)

    def __str__(self):
        return str(self.faculty)

class ProjectComp(models.Model):
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    department = models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),     
    )
    academic_years=models.CharField(verbose_name='Academic Year',max_length=20,choices=academic_year,default="")

    cotypes=(
        ('National','National'),
        ('International','International'),                   
    )
    cotype = models.CharField(max_length=20,choices=cotypes,default="")

    event_types=(
        ('SIH','SIH'),
        ('Avishkar','Avishkar'),    
        ('Others','Others'),                
    )
    event_type = models.CharField(max_length=20,choices=event_types,default="")
    others = models.CharField(verbose_name='',blank=True,max_length=100,default="")

    awards=(
        ('Prize Money','Prize Money'),
        ('Internship','Internship'),    
        ('Certificate','Certificate'),                
    )
    award = models.CharField(max_length=30,choices=awards,default="")

    proof = models.FileField(verbose_name="Proof (only PDF)",upload_to=get_upload_competition,blank=True,default="")

    def __str__(self):
        return str(self.faculty)

class ResearchGrant(models.Model):
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    department = models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),     
    )
    academic_years=models.CharField(verbose_name='Academic Year',max_length=20,choices=academic_year,default="")

    title = models.CharField(verbose_name='Research Title',max_length=100,default="")
    amount = models.PositiveIntegerField(verbose_name="Amount Sanctioned",default=0)
    authority = models.CharField(verbose_name='Granting Authority',max_length=100,default="")
    term = models.PositiveIntegerField(verbose_name="Term of Grant",default=0)

    def __str__(self):
        return str(self.faculty)

class AcademicRR(models.Model):
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    department = models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),     
    )
    academic_years=models.CharField(verbose_name='Academic Year',max_length=20,choices=academic_year,default="")

    syllabussets=(
        ('Syllabus Setting','Syllabus Setting'),
        ('BOS','BOS'), 
        ('Moderator','Moderator'),  
        ('Paper Setter','Paper Setter'),
        ('Reviewer for Journal','Reviewer for Journal'),
        ('Reviewer for Conference','Reviewer for Conference'),  

    )
    syllabusset = models.CharField(verbose_name='Academic Year',max_length=30,choices=syllabussets,default="")

    details = models.CharField(verbose_name='Details of the role',max_length=100,default="")
    proof = models.FileField(verbose_name="Proof (only PDF)",upload_to=get_upload_academicrr,blank=True,default="")

    
    def __str__(self):
        return str(self.faculty)

class PublicationAward(models.Model):
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    department = models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),     
    )
    academic_years=models.CharField(verbose_name='Academic Year',max_length=20,choices=academic_year,default="")

    type_pubs=(
        ('Conference','Conference'),
        ('Journal','Journal'),  
    )
    type_pub = models.CharField(verbose_name='Publication Type',max_length=30,choices=type_pubs,default="")

    title = models.CharField(verbose_name='Title of Publication',max_length=100,default="")
    proof = models.FileField(verbose_name="Proof (only PDF)",upload_to=get_upload_publicationaward,blank=True,default="")

    def __str__(self):
        return str(self.faculty)

class Consultancy(models.Model):
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    department = models.CharField(max_length=50,default="")
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),     
    )
    academic_years=models.CharField(verbose_name='Academic Year',max_length=20,choices=academic_year,default="")

    type_cons=(
        ('National','National'),
        ('International','International'),  
    )
    type_con = models.CharField(verbose_name='Consultancy Type',max_length=30,choices=type_cons,default="")
    orgdet = models.CharField(verbose_name='Organization Details',max_length=300,default="")
    prodet = models.CharField(verbose_name='Project Details',max_length=300,default="")
    start_date = models.DateField(verbose_name='Start Date', default =date.today)

    end_date = models.DateField(verbose_name='End Date', default =date.today)
    durations=models.IntegerField(default=0)
    proof = models.FileField(verbose_name="Proof (only PDF)",upload_to=get_upload_publicationaward,blank=True,default="")

    @property
    def cal_duration(self):
        
        durations = (self.end_date - self.start_date).days
        durations = durations+1
        return durations
    def save(self, *args, **kwarg):
        self.durations = self.cal_duration
        
        super(Consultancy, self).save(*args, **kwarg)
    def __str__(self):
        return str(self.faculty)

class ExpertLecture(models.Model):
    #DEPARTMENT NAME
    department = models.CharField(max_length=50,default="")
    #FACULTY NAME
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    
    #TYPE
    typea = (
        ('Attended','Attended'),
        ('Conducted','Conducted'),
    )
    typeas=models.CharField(verbose_name='Type',max_length=20,choices=typea,default="")

    #ACADEMIC YEAR
    academic_year=(
        ('2020-2021','2020-2021'),
        ('2021-2022','2021-2022'), 
        ('2022-2023','2022-2023'),
        ('2023-2024','2023-2024'),
        ('2024-2025','2024-2025'),     
    )
    academic_years=models.CharField(verbose_name='Academic Year',max_length=20,choices=academic_year,default="")

    resource_person=models.CharField(verbose_name='Name of Resource Person',max_length=20,default="")

    subject=models.CharField(verbose_name='Subject Name',max_length=50,default="")

    topic=models.CharField(verbose_name='Topic',max_length=100,default="")

    year=(
        ('FE','FE'),
        ('SE','SE'),
        ('TE','TE'),
        ('BE','BE'),
    )
    years=models.CharField(verbose_name='Year',max_length=20,choices=year,default="")

    date = models.DateField(verbose_name='Date of Expert Lecture', default =date.today)

    present = models.PositiveIntegerField(verbose_name='Total Students Present',default=0)

    attendance =  models.FileField(verbose_name="Attendance Record (PDF Only)",upload_to=get_upload_expert,default="")

    proof=  models.FileField(verbose_name="Proof",upload_to=get_upload_expert,default="")

    def __str__(self):
        return str(self.faculty)


