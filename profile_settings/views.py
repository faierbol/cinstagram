# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from .models import CinstagramUserSettings
from authentication.models import CinstagramUser


def profile_settings_edit_profile(request):
    """
    In this page the user is able to edit her profile settings such as change
    username, full name, email + add a bio, website url ... etc. and much more
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    empty_credentials = False

    # Get the current user information
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_cinstagram_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
        current_cinstagram_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=current_cinstagram_user
        )
    except ObjectDoesNotExist:
        current_cinstagram_user = None
        current_cinstagram_user_settings = None

    # Edit Profile Form Validation
    if request.POST.get("edit_profile_submit_btn"):
        profile_photo = request.FILES.get("profile_photo")
        full_name = request.POST.get("profile_full_name")
        username = request.POST.get("profile_username")
        personal_url = request.POST.get("profile_url")
        bio = request.POST.get("profile_bio")
        email = request.POST.get("profile_email")
        phone_number = request.POST.get("profile_phone_number")
        gender = request.POST.get("profile_gender")

        if username == "" or email == "":
            # Do not update the model cus there
            # are important empty input fields
            empty_credentials = True
        else:
            # Update the cinstagram user settings model
            current_cinstagram_user_settings.profile_photo = profile_photo
            current_cinstagram_user_settings.full_name = full_name
            current_cinstagram_user_settings.username = username
            current_cinstagram_user_settings.personal_url = personal_url
            current_cinstagram_user_settings.bio = bio
            current_cinstagram_user_settings.email = email
            current_cinstagram_user_settings.phone_number = phone_number
            current_cinstagram_user_settings.gender = gender
            current_cinstagram_user_settings.save()

            # Update the cinstagram user model
            current_cinstagram_user.email = email
            current_cinstagram_user.username = username
            current_cinstagram_user.full_name = full_name
            current_cinstagram_user.save()

    data = {
        "empty_credentials": empty_credentials,
        "current_cinstagram_user": current_cinstagram_user,
        "current_cinstagram_user_settings": current_cinstagram_user_settings,
    }

    return render(request, "profile_settings/edit_profile.html", data)


def profile_settings_change_password(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile_settings/change_password.html", data)


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
