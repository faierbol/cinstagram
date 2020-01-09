from django.urls import path, include
from . import views

urlpatterns = [
    # Profile Posts Page
    path("profile/posts/", views.profile_posts_page, name="profile_posts_page"),
    # Proifle Single Posts Page
    path("profile/posts/<int:post_id>/", views.profile_single_post_page, name="profile_single_post_page"),
    # Profile Likers
    path("profile/posts/<int:post_id>/likers/", views.profile_post_likers, name="profile_post_likers"),
    # Profile Followers
    path("profile/followers/", views.profile_followers, name="profile_followers"),
    # Profile Following
    path("profile/following/", views.profile_following, name="profile_following"),
    # Profile Saved
    path("profile/saved/", views.profile_saved, name="profile_saved"),
    # Profile Tagged
    path("profile/tagged/", views.profile_tagged, name="profile_tagged"),

    # ...
    # Therea are mor urls to be added see the views.py bottom part ...
]
