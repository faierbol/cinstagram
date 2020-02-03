# Main Imports

# Django Imports
from django.db import models
from django.utils import timezone

# My Module Imports
from authentication.models import CinstagramUser


# Follower/d
# -------------
# This model holds the accounts that fallow an account and also the owner
# account that is being followed
class UserFollowing(models.Model):
    # Follower account info
    followed_id = models.IntegerField(blank=False, null=False)
    followed_user = models.ForeignKey(
        CinstagramUser, on_delete=models.CASCADE, related_name="followed_user",
        null=True, blank=True
    )
    # Followed account info
    follower_id = models.IntegerField(blank=False, null=False)
    follower_user = models.ForeignKey(
        CinstagramUser, on_delete=models.CASCADE, related_name="follower_user",
        null=True, blank=True
    )

    def __str__(self):
        return "Followed account: (id: %s) %s | Follower account: (id: %s) %s"\
                % (self.followed_id, self.followed_user,
                   self.follower_id, self.follower_user)
