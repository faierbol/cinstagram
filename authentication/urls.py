from django.urls import path, include
from . import views

urlpatterns = [
    # Signup
    path("auth/signup/", views.authentication_signup, name="authentication_signup"),
    # Login
    path("auth/login/", views.authentication_login, name="authentication_login"),
    # legal
    path("auth/legal/", views.authentication_legal, name="authentication_legal"),
    # Android Setup
    path("help_docs/android_setup/", views.android_setup, name="android_setup"),
    # IOS Setup
    path("help_docs/ios_setup/", views.ios_setup, name="ios_setup"),
    # Forgot Password
    path("auth/forgot_password/", views.forgot_password, name="forgot_password"),
    # Thank you, redirection Page

    # Initial Profile Settings

]
