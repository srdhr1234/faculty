from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name='dashboard'
urlpatterns = [
    path('', views.main, name='main'),
    path('display/',views.display,name='display'),
    path('add/',views.add,name='add'),
    path('stat/',views.statistic,name='statistic'),
    path('display_all/',views.displayAll,name='display_all'),
    path('update/<int:id>/',views.update, name='update'),
    path('data/',views.data,name='data'),
    path('delete/<int:id>/',views.delete_data, name="delete_data"), 
    path('displayall_hod/',views.displayAll_hod,name='displayall_hod'),
    path('stat_hod/',views.statistic_hod,name='statistic_hod'),
    path('upload_ach/',views.upload_ach,name='upload_ach'),
    path('display_ach/',views.display_ach, name="display_ach"),
    path('delete_ach/<int:id>/',views.delete_ach, name="delete_ach"),

    path('statoverall/',views.statistic_overall,name='statistic_overall'),
    path('myprofile/',views.addmyprofile,name='addmyprofile'),
    
    path('viewprofile/',views.viewprofile,name='viewprofile'),

    path('viewmyprofile/',views.viewmyprofile,name='viewmyprofile'),

    path('updatemyprofile/<int:id>/',views.updatemyprofile, name='updatemyprofile'),

    path('excel',views.excel, name="excel"),  
    path('pdf',views.pdf, name="pdf"),

    path('pdf_indi',views.pdf_indi, name="pdf_indi"),
    path('excel_indi',views.excel_indi, name="excel_indi"), 

    path('addcompe/',views.addcompe,name='addcompe'),
    path('displaycompe/',views.displaycompe,name='displaycompe'),
    path('displaycompeh/',views.displaycompeh,name='displaycompeh'),

    path('addresearchgrant/',views.addresearchgrant,name='addresearchgrant'),
    path('displayresearchgrant/',views.displayresearchgrant,name='displayresearchgrant'),
    path('displayrghod/',views.displayrghod,name='displayrghod'),

    path('addacademicrr/',views.addacademicrr,name='addacademicrr'),
    path('displayacademicrr/',views.displayacademicrr,name='displayacademicrr'),
    path('displayacademicrhod/',views.displayacademicrhod,name='displayacademicrhod'),

    path('addpubaward/',views.addpubaward,name='addpubaward'),
    path('displaypubaward/',views.displaypubaward,name='displaypubaward'),
    path('displaypubawardhod/',views.displaypubawardhod,name='displaypubawardhod'),

    path('addconsultancy/',views.addconsultancy,name='addconsultancy'),
    path('displayconsultancy/',views.displayconsultancy,name='displayconsultancy'),
    path('displaypubawardhod/',views.displaypubawardhod,name='displaypubawardhod'),

    path('addexpert/',views.addexpert,name='addexpert'),
    path('displayexpert/',views.displayexpert,name='displayexpert'),
    path('displayexperthod/',views.displayexperthod,name='displayexperthod'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)