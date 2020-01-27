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
    # Edit Profile -- settings
    id = models.AutoField(primary_key=True)
    settings_owner = models.ForeignKey(CinstagramUser, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        upload_to="profile_photo/", blank=True, null=True
    )
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=False, null=False)
    personal_url = models.CharField(max_length=1000)
    bio = models.TextField()
    email = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=100)

    # Email & SMS -- settings
    feedback_emails = models.BooleanField(default=False)
    remainder_emails = models.BooleanField(default=False)
    prodcut_emails = models.BooleanField(default=False)
    news_emails = models.BooleanField(default=False)
    sms_notifications = models.BooleanField(default=False)

    # Privacy & Security -- settings
    private_account = models.BooleanField(default=False)
    turn_off_comments = models.BooleanField(default=False)

    def __str__(self):
        return "Settings id: " + str(self.id) + " | User: " \
                + str(self.settings_owner)
