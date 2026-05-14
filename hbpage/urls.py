# hbpage\urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static 
from .views import delete_inquiry

from .views import (
    homePage,
    aboutUs,
    contactUs,
    galleryPage,
    admission_view,
    dashboardPage,
    loginUser,
    logoutUser,
    delete_admission,
    register_student
)

urlpatterns = [

    # Main Pages
    path('', homePage, name="home"),
    path('about/', aboutUs, name="about"),
    path('contact/', contactUs, name="contact"),
    path('gallery/', galleryPage, name="gallery"),
    path('admission/', admission_view, name="admission"),
    path('dashboard/', dashboardPage, name="dashboard"),

    # Authentication
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('dashboard/delete/<int:pk>/', delete_admission, name="delete_admission"),
    path('register/', register_student, name='register_student'),
    
    
    path('delete-inquiry/<int:id>/', delete_inquiry, name='delete_inquiry'),

    # =========================
    # PASSWORD RESET SYSTEM
    # =========================

    # Enter Email
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            email_template_name='registration/password_reset_email.html',
            subject_template_name='registration/password_reset_subject.txt',
        ),
        name='password_reset'
    ),

    # Email Sent Page
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # Password Reset Confirm
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    # Password Reset Complete
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)