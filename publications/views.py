from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Publication_C, Publication_J, BookChapter, Book, Patent, Copyright
from .forms import Publication_CForm,Publication_JForm, BookChapterForm, BookForm, PatentForm, CopyrightForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import io


import pdfkit
from django.template import loader
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
import xlwt


# Create your views here.

@login_required
def pub_c(request):
    if request.method=="POST":
        form = Publication_CForm(request.POST or None,request.FILES)
        if request.POST:
            val = request.POST.get('scopus', False)
            if val == "Yes":
                form.fields['scopus_value'].required = True
        if form.is_valid():
            instance= form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()  
            return redirect('dashboard:main')
    else:
        form = Publication_CForm()
    return render(request,'publications/pubc.html',{'form':form})


@login_required
def pub_j(request):
    if request.method=="POST":
        form = Publication_JForm(request.POST or None,request.FILES)
        if request.POST:
            val = request.POST.get('scopus', False)
            if val == "Yes":
                form.fields['scopus_value'].required = True
        if form.is_valid():
            instance=form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()
            return redirect('dashboard:main')
    else:
        form = Publication_JForm()
    return render(request,'publications/pubj.html',{'form':form})



@login_required
def bookchapter(request):
    if request.method=="POST":
        form = BookChapterForm(request.POST or None,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()
            return redirect('dashboard:main')
    else:
        form = BookChapterForm()
    return render(request,'publications/bookchapter.html',{'form':form})



@login_required
def book(request):
    if request.method=="POST":
        form = BookForm(request.POST or None,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()
            return redirect('dashboard:main')
    else:
        form = BookForm()
    return render(request,'publications/book.html',{'form':form})


@login_required
def patent(request):
    if request.method=="POST":
        form = PatentForm(request.POST or None,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()
            return redirect('dashboard:main')
    else:
        form = PatentForm()
    return render(request,'publications/patent.html',{'form':form})



@login_required
def copyright(request):
    if request.method=="POST":
        form = CopyrightForm(request.POST or None,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.faculty = request.user
            instance.department = request.user.profile.dept
            instance.save()
            return redirect('dashboard:main')
    else:
        form = CopyrightForm()
    return render(request,'publications/copyright.html',{'form':form})



@login_required
def display_p(request):
    con = Publication_C.objects.filter(faculty= request.user)
    jor = Publication_J.objects.filter(faculty=request.user)
    bookc = BookChapter.objects.filter(faculty=request.user)
    book = Book.objects.filter(faculty=request.user)
    patent = Patent.objects.filter(faculty=request.user)
    copy = Copyright.objects.filter(faculty=request.user)
    
    context ={
        'con':con,
        'jor':jor,
        'bookc':bookc,
        'book':book,
        'patent':patent,
        'copy':copy,

    }
    return render(request,'publications/displayp.html',context)


@login_required
#@user_passes_test(lambda u: u.groups.filter(name='admin').exists())
def displayAllHod(request):

    con = Publication_C.objects.filter(department=request.user.profile.dept).order_by('faculty')
    jor = Publication_J.objects.filter(department=request.user.profile.dept).order_by('faculty')
    bookc = BookChapter.objects.filter(department=request.user.profile.dept).order_by('faculty')
    book = Book.objects.filter(department=request.user.profile.dept).order_by('faculty')
    patent = Patent.objects.filter(department=request.user.profile.dept).order_by('faculty')
    copy = Copyright.objects.filter(department=request.user.profile.dept).order_by('faculty')
    
    context ={
        'con':con,
        'jor':jor,
        'bookc':bookc,
        'book':book,
        'patent':patent,
        'copy':copy,       
        
    }
    return render(request,'publications/displayAllHod.html',context)


@login_required
#@user_passes_test(lambda u: u.groups.filter(name='admin').exists())
def displayAllp(request):
    

    con = Publication_C.objects.all().order_by('faculty')
    jor = Publication_J.objects.all().order_by('faculty')
    bookc = BookChapter.objects.all().order_by('faculty')
    book = Book.objects.all().order_by('faculty')
    patent = Patent.objects.all().order_by('faculty')
    copy = Copyright.objects.all().order_by('faculty')

    
    
    context ={
        'con':con,
        'jor':jor,
        'bookc':bookc,
        'book':book,
        'patent':patent,
        'copy':copy,   
        
    }
    return render(request,'publications/displayAllp.html',context)


@login_required
def updatec(request,id):
    conu = Publication_C.objects.get(id=id)
    form = Publication_CForm(request.POST or None, request.FILES or None, instance=conu)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('publications:displayp')
    return render(request,'publications/pubc.html',{'form':form})


@login_required
def updatej(request,id):
    joru = Publication_J.objects.get(id=id)
    form = Publication_JForm(request.POST or None, request.FILES or None, instance=joru)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('publications:displayp')
    return render(request,'publications/pubj.html',{'form':form})


@login_required
def updatebc(request,id):
    bookcu = BookChapter.objects.get(id=id)
    form = BookChapterForm(request.POST or None, request.FILES or None, instance=bookcu)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('publications:displayp')
    return render(request,'publications/bookchapter.html',{'form':form})


@login_required
def updateb(request,id):
    booku = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=booku)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('publications:displayp')
    return render(request,'publications/book.html',{'form':form})


@login_required
def updatep(request,id):
    patentu = Patent.objects.get(id=id)
    form = PatentForm(request.POST or None, request.FILES or None, instance=patentu)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('publications:displayp')
    return render(request,'publications/patent.html',{'form':form})


@login_required
def updateco(request,id):
    copyu = Copyright.objects.get(id=id)
    form = CopyrightForm(request.POST or None, request.FILES or None, instance=copyu)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('publications:displayp')
    return render(request,'publications/copyright.html',{'form':form})



@login_required
def statisticpub_hod(request):
    if request.POST:
        years = request.POST.get('years', False)       
    else:
        years="2020-2021"
                  
    pubcons={}
    pubjors={}
    bookchaps={} 
    bookks={}
    patentts={}
    copyrightts={}
   
    all_user = User.objects.all().exclude(is_superuser=True).exclude(username="admin")
    
    for user in all_user:
       
        u = user
        pubcon = Publication_C.objects.filter(faculty=user,academic_years=years).count()
        pubcons.update({u:pubcon})
        pubjor = Publication_J.objects.filter(faculty=user,academic_years=years).count()
        pubjors.update({u:pubjor})

        bookchap = BookChapter.objects.filter(faculty=user,academic_years=years).count()
        bookchaps.update({u:bookchap})

        bookk = Book.objects.filter(faculty=user,academic_years=years).count()
        bookks.update({u:bookk})

        patentt = Patent.objects.filter(faculty=user,academic_years=years).count()
        patentts.update({u:patentt})

        copyrightt = Copyright.objects.filter(faculty=user,academic_years=years).count()
        copyrightts.update({u:copyrightt})
        
    
    context ={
        'all_user':all_user,
        'u':u,
        'pubcons':pubcons,
        'pubjors':pubjors,
        'bookchaps':bookchaps,
        'bookks':bookks,
        'patentts':patentts,
        'copyrightts':copyrightts,
        
    } 
    return render(request,'publications/statisticpub_hod.html',context)


@login_required
def statisticpub(request):
    if request.POST:
        years = request.POST.get('years', False)   
        dep = request.POST.get('dep',False)    
    else:
        years="2020-2021"
        dep="Civil"
                  
    pubcons={}
    pubjors={}
    bookchaps={} 
    bookks={}
    patentts={}
    copyrightts={}
   
    all_user = User.objects.all().exclude(is_superuser=True).exclude(username="admin")
    
    for user in all_user:
       
        u = user
        pubcon = Publication_C.objects.filter(faculty=user,academic_years=years).count()
        pubcons.update({u:pubcon})
        pubjor = Publication_J.objects.filter(faculty=user,academic_years=years).count()
        pubjors.update({u:pubjor})

        bookchap = BookChapter.objects.filter(faculty=user,academic_years=years).count()
        bookchaps.update({u:bookchap})

        bookk = Book.objects.filter(faculty=user,academic_years=years).count()
        bookks.update({u:bookk})

        patentt = Patent.objects.filter(faculty=user,academic_years=years).count()
        patentts.update({u:patentt})

        copyrightt = Copyright.objects.filter(faculty=user,academic_years=years).count()
        copyrightts.update({u:copyrightt})
        
    
    context ={
        'all_user':all_user,
        'u':u,
        'pubcons':pubcons,
        'pubjors':pubjors,
        'bookchaps':bookchaps,
        'bookks':bookks,
        'patentts':patentts,
        'copyrightts':copyrightts,
        'dep':dep,
        
    } 
    return render(request,'publications/statisticpub.html',context)

#All department count
@login_required
def statistic_overallp(request):
    if request.POST:
        years = request.POST.get('years', False)        
    else:
        years="2020-2021"
                   
    pubcons={}
    pubjors={}
    bookchaps={} 
    bookks={}
    patentts={}
    copyrightts={}    
    
   
    all_user = User.objects.all().exclude(is_superuser=True).exclude(username="admin")

    departm = ['Civil', 'CMPN', 'EXTC', 'IT', 'Mechanical', 'FE']
    
    
    for deptm in departm:
        
        pubcon = Publication_C.objects.filter(department=deptm,academic_years=years).count()
        pubcons.update({deptm:pubcon})
        pubjor = Publication_J.objects.filter(department=deptm,academic_years=years).count()
        pubjors.update({deptm:pubjor})

        bookchap = BookChapter.objects.filter(department=deptm,academic_years=years).count()
        bookchaps.update({deptm:bookchap})

        bookk = Book.objects.filter(department=deptm,academic_years=years).count()
        bookks.update({deptm:bookk})

        patentt = Patent.objects.filter(department=deptm,academic_years=years).count()
        patentts.update({deptm:patentt})

        copyrightt = Copyright.objects.filter(department=deptm,academic_years=years).count()
        copyrightts.update({deptm:copyrightt})

        
    
    context ={
        
        'departm':departm,
        'pubcons':pubcons,
        'pubjors':pubjors,
        'bookchaps':bookchaps,
        'bookks':bookks,
        'patentts':patentts,
        'copyrightts':copyrightts,
                      
    } 
    return render(request,'publications/statistic_overallp.html',context)


@login_required
def deletec(request,id):
    conu = Publication_C.objects.get(id=id)
   
    if request.method=='POST':
        conu.delete()
        return redirect('publications:displayp')
    return render(request,'publications/delete.html',{'conu':conu})


@login_required
def deletej(request,id):
    joru = Publication_J.objects.get(id=id)
   
    if request.method=='POST':
        joru.delete()
        return redirect('publications:displayp')
    return render(request,'publications/delete.html',{'joru':joru})


@login_required
def deletebc(request,id):
    bookcu = BookChapter.objects.get(id=id)
   
    if request.method=='POST':
        bookcu.delete()
        
        return redirect('publications:displayp')
    return render(request,'publications/delete.html',{'bookcu':bookcu})


@login_required
def deleteb(request,id):
    booku = Book.objects.get(id=id)
  
    if request.method=='POST':
        booku.delete()
        
        return redirect('publications:displayp')
    return render(request,'publications/delete.html',{'booku':booku})


@login_required
def deletep(request,id):
    patentu = Patent.objects.get(id=id)
  
    if request.method=='POST':
        patentu.delete()
        
        return redirect('publications:displayp')
    return render(request,'publications/delete.html',{'patentu':patentu})


@login_required
def deleteco(request,id):
    copyu = Copyright.objects.get(id=id)
  
    if request.method=='POST':
        copyu.delete()
        
        return redirect('publications:displayp')
    return render(request,'publications/delete.html',{'copyu':copyu})

@login_required
def pdfp(request):
    con = Publication_C.objects.filter(department=request.user.profile.dept).order_by('-academic_years')
    jor = Publication_J.objects.filter(department=request.user.profile.dept).order_by('-academic_years')
    bookc = BookChapter.objects.filter(department=request.user.profile.dept).order_by('-academic_years')
    book = Book.objects.filter(department=request.user.profile.dept).order_by('-academic_years')
    patent = Patent.objects.filter(department=request.user.profile.dept).order_by('-academic_years')
    copy = Copyright.objects.filter(department=request.user.profile.dept).order_by('-academic_years')
    
    
    template = loader.get_template('publications/pdfHod.html')
    
    html = template.render({'con':con, 'jor':jor, 'bookc':bookc, 'book':book, 'patent':patent, 'copy':copy})
 
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