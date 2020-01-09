# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports


def profile_settings_change_password(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile_settings/change_password.html", data)


def profile_settings_edit_profile(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile_settings/edit_profile.html", data)


def profile_settings_email_sms(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile_settings/email_sms.html", data)


def profile_settings_privacy_security(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile_settings/privacy_security.html", data)
