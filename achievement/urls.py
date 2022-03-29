
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as authentication_views
from dashboard import views as user_views
from django.conf import settings
from django.conf.urls.static import static

# Django admin header configuration
admin.site.site_header="Faculty Portal"
admin.site.site_title="Faculty Portal"
admin.site.index_title="Admin for Faculty Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('dashboard.urls')),
    path('',include('publications.urls')),
    path('',authentication_views.LoginView.as_view(template_name='dashboard/login.html'),name='login'),
    
    path('logout/',authentication_views.LogoutView.as_view(template_name='dashboard/logout.html'),name='logout'),

    # reset password urls
    path('reset_password/', authentication_views.PasswordResetView.as_view(template_name='dashboard/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', authentication_views.PasswordResetDoneView.as_view(template_name='dashboard/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', authentication_views.PasswordResetConfirmView.as_view(template_name='dashboard/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', authentication_views.PasswordResetCompleteView.as_view(template_name='dashboard/password_reset_done.html'), name="password_reset_complete"),
    
    path('password_change/',authentication_views.PasswordChangeView.as_view(template_name='dashboard/password_change.html'), name='password_change'),
    path('password_change_done/',authentication_views.PasswordChangeDoneView.as_view(template_name='dashboard/password_change_done.html'), name='password_change_done'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
