from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .filters import *
import pdfkit
from django.template import loader
import io
import datetime
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import xlwt

#main page

@login_required
def main(request):
    lst = {}
    img = Show_Achieve.objects.all()
    all_user = User.objects.all()
    bday = MyProfile.objects.all()
    cmonth = datetime.date.today().month
    cday = datetime.date.today().day
 
    context ={
        'img':img,
        'cmonth':cmonth,
        'cday':cday, 
        'bday':bday,
        'all_user':all_user,      
    }
    return render(request,'dashboard/main.html',context)

@login_required
def upload_ach(request):
    if request.method == 'POST':
        form = Show_AchieveForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()   
            return redirect('dashboard:main')
    else:
        form = Show_AchieveForm()
    return render(request,'dashboard/upload_ach.html',{'form':form})


#Form to add data
@login_required
def add(request):
    
    if request.method == 'POST':
        form = DataForm(request.POST or None,request.FILES)
        if request.POST:
            val = request.POST.get('events', False)
            if val == "Others":
                form.fields['others'].required = True
                
        if form.is_valid():  
            
            instance= form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()  
            return redirect('dashboard:main')
    else:
        form = DataForm()
    return render(request,'dashboard/add_data.html',{'form':form})

@login_required
def addmyprofile(request):

    all_user = User.objects.all()
    if request.method == 'POST':
        form = MyProfileForm(request.POST or None,request.FILES)
        if MyProfile.objects.filter(faculty__in=all_user).exists():
            messages.error(request,"User Profile already exists")
        else:
            if form.is_valid():  
                
                instance= form.save(commit=False)
                instance.faculty = request.user
                instance.department = request.user.profile.dept
                instance.form_submitted = True
                instance.save()  
                return redirect('dashboard:main')
    else:
        form = MyProfileForm()

    context={
        'form':form,
            
    }
    return render(request,'dashboard/addmyprofile.html',context)

@login_required
def viewmyprofile(request):
    profile = MyProfile.objects.filter(faculty= request.user)
    context ={
        'profile':profile,

    }
    return render(request,'dashboard/viewmyprofile.html',context)

@login_required
def updatemyprofile(request,id):

    item = MyProfile.objects.get(id=id)
    form = MyProfileForm(request.POST or None,request.FILES or None, instance=item)
    if form.is_valid(): 
        edit = form.save(commit=False) 
        edit.save()
        return redirect('dashboard:viewmyprofile')
    return render(request,'dashboard/addmyprofile.html',{'form':form,'item':item})


#update value to form
@login_required
def update(request,id):
    item = Details.objects.get(id=id)
    form = DataForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('dashboard:display')
    return render(request,'dashboard/add_data.html',{'form':form})


#delete data from records
@login_required
#@user_passes_test(lambda u: u.groups.filter(name='admin').exists())
def delete_data(request,id):
    del_data = Details.objects.get(id=id)
    if request.method=='POST':
        del_data.delete()
        return redirect('dashboard:displayall_hod')
    return render(request,'dashboard/delete_data.html',{'del_data':del_data})


@login_required
def viewprofile(request):

    display  = MyProfile.objects.all()
    context ={
        'display':display,
       

    }
    return render(request,'dashboard/viewprofile.html',context)

#display individual data
@login_required
def display(request):
    listt = Details.objects.filter(faculty= request.user).order_by('-academic_years')
    myFilter2 = DetailsFilter_indi(request.GET,queryset=listt)
    listt = myFilter2.qs 
    context ={
        'listt':listt,
        'myFilter2':myFilter2,

    }
    return render(request,'dashboard/display.html',context)


#display all data by management
@login_required
#@user_passes_test(lambda u: u.groups.filter(name='admin').exists())
def displayAll(request):
    
    dis_all = Details.objects.all().order_by('faculty')
    myFilter = DetailsFilter(request.GET,queryset=dis_all)
    
    dis_all = myFilter.qs    
    context ={
        'dis_all':dis_all,
        'myFilter':myFilter,         
        
    }
    return render(request,'dashboard/displayAll.html',context)


#display data to download
@login_required
def data(request):
    data = Details.objects.all().order_by('faculty')

    context={
        'data':data,
    }
    return render(request,'dashboard/data.html',context)


@login_required
#@user_passes_test(lambda u: u.groups.filter(name='admin').exists())
def displayAll_hod(request):
    
    dis_all = Details.objects.filter(department=request.user.profile.dept).order_by('-academic_years','faculty')
    myFilter1 = DetailsFilter_hod(request.GET,queryset=dis_all)
    
    dis_all = myFilter1.qs    
    context ={
        'dis_all':dis_all,
        'myFilter1':myFilter1,         
        
    }    
    return render(request,'dashboard/displayAll_hod.html',context)
#all_user = Details.objects.filter(department=request.user.profile.dept)


@login_required
#@user_passes_test(lambda u: u.groups.filter(name='admin').exists())
def display_ach(request):
    dis_ach = Show_Achieve.objects.all()
    context ={
        'dis_ach':dis_ach,
                
        
    }
    return render(request,'dashboard/display_ach.html',context)

@login_required
#@user_passes_test(lambda u: u.groups.filter(name='admin').exists())
def delete_ach(request,id):
    del_ach = Show_Achieve.objects.get(id=id)
    if request.method=='POST':
        del_ach.delete()
        return redirect('dashboard:display_ach')
    return render(request,'dashboard/delete_ach.html',{'del_ach':del_ach})

#display statistics
@login_required
def statistic(request):
    if request.POST:
        years = request.POST.get('years', False)
        dep = request.POST.get('dep',False)
        
    else:
        years="2020-2021"
        dep="Civil"     
        
    sttps={}
    fdps={}
    webinars={}
    nptels={}
    udemys={}
    totals={}
    ongoings={}
    completeds={}
    rnds={}
    fops={}
    
    courseras={}
    others={}
        
   
    all_user = User.objects.all().exclude(is_superuser=True).exclude(username="admin")
 
    for user in all_user:
        u = user
        total = Details.objects.filter(faculty=user,academic_years=years).count()
        totals.update({u:total})
        sttp = Details.objects.filter(faculty=user,academic_years=years,events='STTP').count()
        sttps.update({u:sttp})
        fdp = Details.objects.filter(faculty=user,academic_years=years,events='FDP').count()
        fdps.update({u:fdp})
        webinar = Details.objects.filter(faculty=user,academic_years=years,events='Webinar').count()
        webinars.update({u:webinar})
        nptel = Details.objects.filter(faculty=user,academic_years=years,events='NPTEL').count()
        nptels.update({u:nptel})
        udemy = Details.objects.filter(faculty=user,academic_years=years,events='Udemy').count()
        udemys.update({u:udemy})
        rnd = Details.objects.filter(faculty=user,academic_years=years,events='R&D Sessions').count()
        rnds.update({u:rnd})

        fop = Details.objects.filter(faculty=user,academic_years=years,events='Faculty Orienation Program').count()
        fops.update({u:fop})

        #Coursera Course Counts
        coursera = Details.objects.filter(faculty=user,academic_years=years,events='Coursera').count()
        courseras.update({u:coursera})

        #End of count logic

        other = Details.objects.filter(faculty=user,academic_years=years,events='Others').count()
        others.update({u:other})

    
        ongoing = Details.objects.filter(faculty=user,academic_years=years,certificate="").count()
        ongoings.update({u:ongoing})
        completed = Details.objects.filter(faculty=user,academic_years=years).exclude(certificate="").count()
        completeds.update({u:completed})
    
    
    context ={
        'sttp':sttp,
        'all_user':all_user,
        'u':u,
        'sttps':sttps,
        'fdps':fdps,
        'webinars':webinars,
        'nptels':nptels,
        'udemys':udemys,
        'rnds':rnds,
        'totals':totals,
        'ongoings':ongoings,
        'completeds':completeds,
        'total':total,  
        'dep':dep,  
        'fops':fops, 

        'courseras':courseras,
        'others':others,       

    }  
    return render(request,'dashboard/statistics.html',context)

#display statistics to hods
@login_required
def statistic_hod(request):
    if request.POST:
        years = request.POST.get('years', False)        
    else:
        years="2020-2021"
                   
    sttps={}
    fdps={}
    webinars={}
    nptels={}
    udemys={}
    totals={}
    ongoings={}
    completeds={}
    rnds={}
    fops={}

    courseras={}
    others={}
 
    all_user = User.objects.all().exclude(is_superuser=True).exclude(username="admin")
    
    
    for user in all_user:
       
        u = user
        total = Details.objects.filter(faculty=user,academic_years=years).count()
        totals.update({u:total})
        sttp = Details.objects.filter(faculty=user,academic_years=years,events='STTP').count()
        sttps.update({u:sttp})
        fdp = Details.objects.filter(faculty=user,academic_years=years,events='FDP').count()
        fdps.update({u:fdp})
        webinar = Details.objects.filter(faculty=user,academic_years=years,events='Webinar').count()
        webinars.update({u:webinar})
        nptel = Details.objects.filter(faculty=user,academic_years=years,events='NPTEL').count()
        nptels.update({u:nptel})
        udemy = Details.objects.filter(faculty=user,academic_years=years,events='Udemy').count()
        udemys.update({u:udemy})
        rnd = Details.objects.filter(faculty=user,academic_years=years,events='R&D Sessions').count()
        rnds.update({u:rnd})

        fop = Details.objects.filter(faculty=user,academic_years=years,events='Faculty Orienation Program').count()
        fops.update({u:fop})
        
        #Coursera Course Counts
        coursera = Details.objects.filter(faculty=user,academic_years=years,events='Coursera').count()
        courseras.update({u:coursera})
        #End of count logic

        other = Details.objects.filter(faculty=user,academic_years=years,events='Others').count()
        others.update({u:other})

        
        ongoing = Details.objects.filter(faculty=user,academic_years=years,certificate="").count()
        ongoings.update({u:ongoing})
        completed = Details.objects.filter(faculty=user,academic_years=years).exclude(certificate="").count()
        completeds.update({u:completed})
        
    
    context ={
        'sttp':sttp,
        'all_user':all_user,
        'u':u,
        'sttps':sttps,
        'fdps':fdps,
        'webinars':webinars,
        'nptels':nptels,
        'udemys':udemys,
        'rnds':rnds,
        'totals':totals,
        'ongoings':ongoings,
        'completeds':completeds,
        'total':total, 
        'fops':fops,

        'courseras':courseras,
        'others':others,                    
    } 
    return render(request,'dashboard/statistics_hod.html',context)


#All department count
@login_required
def statistic_overall(request):
    if request.POST:
        years = request.POST.get('years', False)        
    else:
        years="2020-2021"
                   
    sttps={}
    fdps={}
    webinars={}
    nptels={}
    udemys={}
    totals={}
    ongoings={}
    completeds={}
    rnds={}
    fops={}

    courseras={}
 
    others={}
       
    all_user = User.objects.all().exclude(is_superuser=True).exclude(username="admin")

    departm = ['CMPN', 'IT']
    
    
    for deptm in departm:
        
        total = Details.objects.filter(department=deptm,academic_years=years).count()
        totals.update({deptm:total})
        sttp = Details.objects.filter(department=deptm,academic_years=years,events='STTP').count()
        sttps.update({deptm:sttp})
        fdp = Details.objects.filter(department=deptm,academic_years=years,events='FDP').count()
        fdps.update({deptm:fdp})
        webinar = Details.objects.filter(department=deptm,academic_years=years,events='Webinar').count()
        webinars.update({deptm:webinar})
        nptel = Details.objects.filter(department=deptm,academic_years=years,events='NPTEL').count()
        nptels.update({deptm:nptel})
        udemy = Details.objects.filter(department=deptm,academic_years=years,events='Udemy').count()
        udemys.update({deptm:udemy})
        rnd = Details.objects.filter(department=deptm,academic_years=years,events='R&D Sessions').count()
        rnds.update({deptm:rnd})
        
        fop = Details.objects.filter(department=deptm,academic_years=years,events='Faculty Orienation Program').count()
        fops.update({deptm:fop})
        #Coursera Course Counts
        coursera = Details.objects.filter(faculty=user,academic_years=years,events='Coursera').count()
        courseras.update({u:coursera})
        #End of count logic

        other = Details.objects.filter(department=deptm,academic_years=years,events='Others').count()
        others.update({deptm:other})

        
        ongoing = Details.objects.filter(department=deptm,academic_years=years,certificate="").count()
        ongoings.update({deptm:ongoing})
        completed = Details.objects.filter(department=deptm,academic_years=years).exclude(certificate="").count()
        completeds.update({deptm:completed})
        
    
    context ={
        
        'departm':departm,
        'sttps':sttps,
        'fdps':fdps,
        'webinars':webinars,
        'nptels':nptels,
        'udemys':udemys,
        'rnds':rnds,
        'totals':totals,
        'ongoings':ongoings,
        'completeds':completeds,
        'total':total, 
        'fops':fops,

        'courseras':courseras,
        'others':others,                    
    } 
    return render(request,'dashboard/statistic_overall.html',context)

@login_required
def pdf(request):
    
    ay = request.GET.get("academic_years",None)
    request.session['val'] = request.GET.get("academic_years",None)
    
    if ay == "":
        dis_all = Details.objects.filter(department=request.user.profile.dept).order_by('faculty')
    else:
        dis_all = Details.objects.filter(department=request.user.profile.dept,academic_years=ay).order_by('faculty')


    template = loader.get_template('dashboard/pdf_data.html')
    
    html = template.render({'dis_all':dis_all})
 
    options ={
        'page-size':'Letter',
        'encoding':'UTF-8',       
        'enable-local-file-access': '',
        'footer-right': '[page] of [topage]',
        
  
    }
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html,False,options,configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    return response

@login_required
def excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="faculty_Data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Faculty Achievement')
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.alignment.wrap = 1

    columns = ['Faculty First Name', 'Faculty Last Name', 'Academic Year', 'Type', 'Event Description', 'Title', 'College Name', 'Start Date', 'End Date', 'Duration of Course']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
        ws.col(col_num).width = int(5000)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
   
   
    
    ay = request.GET.get("academic_years",None)
    if ay == "":
        rows = Details.objects.filter(department=request.user.profile.dept).order_by('-academic_years').values_list('faculty__first_name', 'faculty__last_name', 'academic_years', 'typeas','events', 'topic', 'college_name', 'start_date', 'end_date', 'durations')
    else:
        rows = Details.objects.filter(department=request.user.profile.dept,academic_years=ay).order_by('-academic_years').values_list('faculty__first_name', 'faculty__last_name', 'academic_years', 'typeas','events', 'topic', 'college_name', 'start_date', 'end_date', 'durations')
    
    
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    
    wb.save(response)
    return response


@login_required
def pdf_indi(request):
    
    ay = request.GET.get("academic_years",None)
    if ay == "":
        dis_all = Details.objects.filter(faculty= request.user).order_by('-academic_years')
    else:
        dis_all = Details.objects.filter(faculty= request.user,academic_years=ay).order_by('-academic_years')

    template = loader.get_template('dashboard/pdf_indi.html')
    
    html = template.render({'dis_all':dis_all, 'ay':ay})
 
    options ={
        'page-size':'Letter',
        'encoding':'UTF-8',       
        'enable-local-file-access': '',
        'footer-right': '[page] of [topage]',
        
  
    }
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html,False,options,configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    return response

@login_required
def excel_indi(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="faculty_Data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Faculty Achievement')
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.alignment.wrap = 1

    columns = ['Academic Year', 'Type', 'Event Description', 'Title', 'College Name', 'Start Date', 'End Date', 'Duration of Course']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
        ws.col(col_num).width = int(5000)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
   
   
    
    ay = request.GET.get("academic_years",None)
    if ay == "":
        rows = Details.objects.filter(faculty= request.user).order_by('-academic_years').values_list('academic_years', 'typeas','events', 'topic', 'college_name', 'start_date', 'end_date', 'durations')
    else:
        rows = Details.objects.filter(faculty= request.user,academic_years=ay).order_by('-academic_years').values_list('academic_years', 'typeas','events', 'topic', 'college_name', 'start_date', 'end_date', 'durations')
    
    
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    
    wb.save(response)
    return response

@login_required
def addcompe(request):
    
    if request.method == 'POST':
        form = ProjectCompForm(request.POST or None,request.FILES)
        if request.POST:
            val = request.POST.get('event_type', False)
            if val == "Others":
                form.fields['others'].required = True
                
        if form.is_valid():  
            
            instance= form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()  
            return redirect('dashboard:main')
    else:
        form = ProjectCompForm()
    return render(request,'dashboard/add_comp.html',{'form':form})

@login_required
def displaycompe(request):
    compe = ProjectComp.objects.filter(faculty= request.user).order_by('-academic_years')
    
    context ={
        'compe':compe,

    }
    return render(request,'dashboard/display_compe.html',context)

@login_required
def displaycompeh(request):
    compeh = ProjectComp.objects.filter(department=request.user.profile.dept).order_by('-academic_years','faculty')
    filtercomh = ProjectCompFilter(request.GET,queryset=compeh)
    
    compeh = filtercomh.qs    
    
    context ={
        'compeh':compeh,
        'filtercomh':filtercomh,

    }
    return render(request,'dashboard/display_compehod.html',context)

@login_required
def addresearchgrant(request):
    
    if request.method == 'POST':
        form = ResearchGrantForm(request.POST or None,request.FILES)
                
        if form.is_valid():  
            
            instance= form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()  
            return redirect('dashboard:main')
    else:
        form = ResearchGrantForm()
    return render(request,'dashboard/add_researchg.html',{'form':form})

@login_required
def displayresearchgrant(request):
    rg = ResearchGrant.objects.filter(faculty= request.user).order_by('-academic_years')
    
    context ={
        'rg':rg,

    }
    return render(request,'dashboard/display_rg.html',context)

@login_required
def displayrghod(request):
    rgh = ResearchGrant.objects.filter(department=request.user.profile.dept).order_by('-academic_years','faculty')
    filterrgh = ResearchGrantFilter(request.GET,queryset=rgh)
    
    rgh = filterrgh.qs    
    
    context ={
        'rgh':rgh,
        'filterrgh':filterrgh,

    }
    return render(request,'dashboard/display_rghod.html',context)

@login_required
def addacademicrr(request):
    
    if request.method == 'POST':
        form = AcademicRRForm(request.POST or None,request.FILES)
                
        if form.is_valid():  
            
            instance= form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()  
            return redirect('dashboard:main')
    else:
        form = AcademicRRForm()
    return render(request,'dashboard/add_academicrr.html',{'form':form})

@login_required
def displayacademicrr(request):
    arr = AcademicRR.objects.filter(faculty= request.user).order_by('-academic_years')
    
    context ={
        'arr':arr,

    }
    return render(request,'dashboard/display_academicrr.html',context)

@login_required
def displayacademicrhod(request):
    arrh = AcademicRR.objects.filter(department=request.user.profile.dept).order_by('-academic_years','faculty')
    filterrrh = ResearchGrantFilter(request.GET,queryset=arrh)
    
    arrh = filterrrh.qs    
    
    context ={
        'arrh':arrh,
        'filterrrh':filterrrh,

    }
    return render(request,'dashboard/display_academicrrhod.html',context)

@login_required
def addpubaward(request):
    
    if request.method == 'POST':
        form = PublicationAwardForm(request.POST or None,request.FILES)
                
        if form.is_valid():  
            
            instance= form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()  
            return redirect('dashboard:main')
    else:
        form = PublicationAwardForm()
    return render(request,'dashboard/add_pubaward.html',{'form':form})


@login_required
def displaypubaward(request):
    pa = PublicationAward.objects.filter(faculty= request.user).order_by('-academic_years')
    
    context ={
        'pa':pa,
    }
    return render(request,'dashboard/display_pubaward.html',context)

@login_required
def displaypubawardhod(request):
    pah = PublicationAward.objects.filter(department=request.user.profile.dept).order_by('-academic_years','faculty')
    filterpah = PublicationAwardFilter(request.GET,queryset=pah)
    
    pah = filterpah.qs    
    
    context ={
        'pah':pah,
        'filterpah':filterpah,

    }
    return render(request,'dashboard/display_pubawardhod.html',context)

@login_required
def addconsultancy(request):
    
    if request.method == 'POST':
        form = ConsultancyForm(request.POST or None,request.FILES)
                
        if form.is_valid():  
            
            instance= form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()  
            return redirect('dashboard:main')
    else:
        form = ConsultancyForm()
    return render(request,'dashboard/add_pubaward.html',{'form':form})

@login_required
def displayconsultancy(request):
    con = Consultancy.objects.filter(faculty= request.user).order_by('-academic_years')
    
    context ={
        'con':con,
    }
    return render(request,'dashboard/display_consult.html',context)

@login_required
def displaypubawardhod(request):
    conh = Consultancy.objects.filter(department=request.user.profile.dept).order_by('-academic_years','faculty')
    filterconh = ConsultancyFilter(request.GET,queryset=conh)
    
    conh = filterconh.qs    
    
    context ={
        'conh':conh,
        'filterconh':filterconh,

    }
    return render(request,'dashboard/display_consulthod.html',context)

@login_required
def addexpert(request):
    
    if request.method == 'POST':
        form = ExpertLectureForm(request.POST or None,request.FILES)
                
        if form.is_valid():  
            
            instance= form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()  
            return redirect('dashboard:main')
    else:
        form = ExpertLectureForm()
    return render(request,'dashboard/add_expert.html',{'form':form})

@login_required
def displayexpert(request):
    expert = ExpertLecture.objects.filter(faculty= request.user).order_by('-academic_years')
    
    context ={
        'expert':expert,
    }
    return render(request,'dashboard/display_expert.html',context)

@login_required
def displayexperthod(request):
    experth = ExpertLecture.objects.filter(department=request.user.profile.dept).order_by('-academic_years','faculty')
    filterexperth = ExpertLectureFilter(request.GET,queryset=experth)
    
    experth = filterexperth.qs    
    
    context ={
        'experth':experth,
        'filterexperth':filterexperth,

    }
    return render(request,'dashboard/display_experthod.html',context)
