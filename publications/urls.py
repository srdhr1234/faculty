from django.urls import path
from .import views

app_name='publications'
urlpatterns = [
    
    path('pub_c/', views.pub_c, name='pubc'),
    path('pub_j/', views.pub_j, name="pubj"),
    path('bookchapter/', views.bookchapter, name="bookchapter"),
    path('book/', views.book, name="book"),
    path('patent/', views.patent, name="patent"),
    path('copyright/', views.copyright, name="copyright"),


    path('display_p/',views.display_p, name="displayp"),
    path('updatec/<int:id>/',views.updatec, name='updatec'),
    path('updatej/<int:id>/',views.updatej, name='updatej'),
    path('updatebc/<int:id>/',views.updatebc, name='updatebc'),
    path('updateb/<int:id>/',views.updateb, name='updateb'),
    path('updatep/<int:id>/',views.updatep, name='updatep'),
    path('updateco/<int:id>/',views.updateco, name='updateco'),
    path('statisticpub',views.statisticpub, name='statisticpub'),


    path('displayAllHod/',views.displayAllHod,name='displayAllHod'),
    path('statpub_hod/',views.statisticpub_hod,name='statisticpub_hod'),
    path('displayAllp/',views.displayAllp,name='displayAllp'),

    path('statoverallp/',views.statistic_overallp, name='statistic_overallp'),

    path('deletec/<int:id>/',views.deletec, name="deletec"), 
    path('deletej/<int:id>/',views.deletej, name="deletej"), 
    path('deletebc/<int:id>/',views.deletebc, name="deletebc"), 
    path('deleteb/<int:id>/',views.deleteb, name="deleteb"), 
    path('deletep/<int:id>/',views.deletep, name="deletep"), 
    path('deleteco/<int:id>/',views.deleteco, name="deleteco"), 

    path('pdfp',views.pdfp, name="pdfp"),
    
    
]