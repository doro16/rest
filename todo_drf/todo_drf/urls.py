"""todo_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys
sys.path.append('C:\rest')
from allauth.account.views import confirm_email
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
)

from todo_drf.users.views import ConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seoul/', include('seoul.urls')),
    path('tb/', include('tb.urls')),
    path('users/', include('users.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

    # 로그인
    path('rest-auth/login', LoginView.as_view(), name='rest_login'),
    path('rest-auth/logout', LogoutView.as_view(), name='rest_logout'),
    path('rest-auth/password/change', PasswordChangeView.as_view(), name='rest_password_change'),

    # 회원가입
    path('rest-auth/registration', RegisterView.as_view(), name='rest_register'),
    path('accounts/', include('allauth.urls')),

    # 이메일 관련 필요 path('accounts/allauth/', include('allauth.urls')),
    # 유효한 이메일이 유저에게 전달
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # 유저가 클릭한 이메일(=링크) 확인
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



