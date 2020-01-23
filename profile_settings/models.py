# Main Imports

# Django Imports
from django.db import models
from django.utils import timezone

# My Module Imports
from authentication.models import CinstagramUser


# User Profile Settings
# -------------
# This model holds the base settings of the user such as email, username .. etc
# more complicated settigns such as privacy, sms ... etc. will be keyed to this
# base model with foreign keys
class CinstagramUserSettings(models.Model):
    id = None
    settings_owner = None
    profile_photo = None
    full_name = None
    username = None
    personal_url = None
    bio = None
    email = None
    phone_number = None
    gender = None

    def __str__(self):
        return "Settings id: " + str(self.id) + " | User: " \
                + str(self.settings_owner)
