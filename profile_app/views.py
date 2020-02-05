# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from authentication.models import CinstagramUser
from profile_settings.models import CinstagramUserSettings
from media_upload.models import UserPhoto, UserPhotoComment, UserPhotoLike
from media_upload.models import UserPhotoBookmark
from .models import UserFollowing


def profile_posts_page(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile/posts_page.html", data)


def profile_single_post_page(request, post_id):
    """
    This view holds all the controller logic for the post system that the usual
    users post. They are generally videos, photos, gifs .. etc.
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    # Get the current user
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
    except ObjectDoesNotExist:
        current_user = None

    # Get the current user settings
    try:
        current_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=current_user
        )
    except ObjectDoesNotExist:
        current_user_settings = None

    # Get the current post object
    try:
        post = UserPhoto.objects.get(id=post_id, user=current_user)
    except ObjectDoesNotExist:
        post = None

    # Get the Post Comments
    try:
        post_comments = UserPhotoComment.objects.all()
    except ObjectDoesNotExist:
        post_comments = None

    # Get the Post Likes
    try:
        post_likes = None
    except ObjectDoesNotExist:
        post_likes = None

    # Post Like form Validation
    if request.POST.get("post_like_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Check if the current use has already liked this picture before
        # if she has, then do not like again since a photo can be only
        # liked once by one person
        try:
            filtered_post_liker = UserPhotoLike.objects.get(
                like_owner=current_user
            )
        except ObjectDoesNotExist:
            filtered_post_liker = None

        if filtered_post_liker == None:
            new_like = UserPhotoLike(like_owner=current_user, liked_photo=post)
            new_like.save()
        else:
            pass  # cant like again

    # Post Bookmark From Validaiton
    if request.POST.get("post_bookmark_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Check if the current user already bookmarked this picture
        # if she has do not bookmark it again since it can only be
        # bookmarked once by one person
        try:
            filtered_post_bookmarker = UserPhotoBookmark.objects.get(
                bookmark_owner=current_user
            )
        except ObjectDoesNotExist:
            filtered_post_bookmarker = None

        if filtered_post_bookmarker == None:
            new_bookmark = UserPhotoBookmark(
                bookmark_owner=current_user, bookmarked_photo=post
            )
            new_bookmark.save()
        else:
            pass  # cant bookmark again

    # Post Comment form Validation
    if request.POST.get("post_comment_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        comment_content = request.POST.get("comment_content")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Create a new comment for the photo
        new_comment = UserPhotoComment(
            comment_owner=current_user,
            comment_owner_settings=current_user_settings,
            commented_photo=post,
            comment=comment_content
        )
        new_comment.save()

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "post": post,
        "post_comments": post_comments,
    }

    return render(request, "profile/post_page.html", data)


def profile_post_likers(request, post_id):
    """
    This page showcases all of the likers of a given user post such as a photo
    video, gallery ... etc.
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    # Get the current user
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
    except ObjectDoesNotExist:
        current_user = None

    # Get the current user settings
    try:
        current_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=current_user
        )
    except ObjectDoesNotExist:
        current_user_settings = None

    # Get the current post object
    try:
        post = UserPhoto.objects.get(id=post_id, user=current_user)
    except ObjectDoesNotExist:
        post = None

    # Get the likers
    try:
        post_likes = UserPhotoLike.objects.all()
    except ObjectDoesNotExist:
        post_likes = None

    # Get the Followers/Followings
    try:
        current_user_followings = UserFollowing.objects.filter(
            follower_user=current_user,
        )
        accounts_current_user_following = []
        for following in current_user_followings:
            accounts_current_user_following.append(following.followed_user)
    except ObjectDoesNotExist:
        current_user_followings = None
        accounts_current_user_following = []

    # Follow Form processing
    if request.POST.get("follow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        hidden_user = CinstagramUser.objects.get(id=hidden_user_id)
        hidden_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=hidden_user
        )
        # Check if the user already has a `follow` relationship with thecurrent
        # user, if there is do nothing. If there is not create new relationship
        try:
            filtered_follower = UserFollowing.objects.get(
                followed_id=hidden_user.id,
                follower_id=current_user.id,
            )
        except ObjectDoesNotExist:
            filtered_follower = None

        if filtered_follower == None:
            # new relationship
            new_following_relationship = UserFollowing(
                followed_id=hidden_user.id,
                followed_user=hidden_user,
                followed_user_settings=hidden_user_settings,
                follower_id=current_user.id,
                follower_user=current_user,
                follower_user_settings=current_user_settings,
            )
            new_following_relationship.save()
            return HttpResponseRedirect("/profile/posts/"+str(post_id)+"/likers/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Un-Follow form processing
    if request.POST.get("unfollow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        hidden_user = CinstagramUser.objects.get(id=hidden_user_id)
        hidden_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=hidden_user
        )
        # Check if the user already has a `follow` relationship with thecurrent
        # user, if there is not do nothing. If there is  delete  relationship
        try:
            filtered_follower = UserFollowing.objects.get(
                followed_id=hidden_user.id,
                follower_id=current_user.id,
            )
        except ObjectDoesNotExist:
            filtered_follower = None

        if filtered_follower == None:
            # do nothing since it does not exists
            pass
        else:
            # delete the relationship
            filtered_follower.delete()
            return HttpResponseRedirect("/profile/posts/"+str(post_id)+"/likers/")

    '''
    SELF NOTE FOR FUTURE AT THE MOMENT I AM NOT IMPLEMENTING THE + BUTTON FORM
    AT THE END OF THE PAGE FOR LOADING MORE DATA, ATM IT JUST LOADS EVERYTHING
    THE TABLE HOLDS. BUT IN THE FUTURE I WILL CHANGE IT SINCE IT IS BAD FOR
    LOADING EVERY ENTRY FROM THE DATA
    '''

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "post": post,
        "post_likes": post_likes,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
    }

    return render(request, "profile/likers.html", data)


def profile_followers(request):
    """
    In this page the user can see all the followers of her account. And she
    can follow or unfollow them.
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    # Get the current user
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
    except ObjectDoesNotExist:
        current_user = None

    # Get the current user settings
    try:
        current_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=current_user
        )
    except ObjectDoesNotExist:
        current_user_settings = None

    # Get the Acounts Current User is Following
    try:
        current_user_followings = UserFollowing.objects.filter(
            follower_user=current_user,
        )
        accounts_current_user_following = []
        for following in current_user_followings:
            accounts_current_user_following.append(following.followed_user)
    except ObjectDoesNotExist:
        current_user_followings = None
        accounts_current_user_following = []

    # Get the Accounts that Follow Current User
    try:
        accounts_following_current_user = UserFollowing.objects.filter(
            followed_user=current_user,
        )
    except ObjectDoesNotExist:
        accounts_following_current_user = None

    # Follow Form processing
    if request.POST.get("follow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        hidden_user = CinstagramUser.objects.get(id=hidden_user_id)
        hidden_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=hidden_user
        )
        # Check if the user already has a `follow` relationship with thecurrent
        # user, if there is do nothing. If there is not create new relationship
        try:
            filtered_follower = UserFollowing.objects.get(
                followed_id=hidden_user.id,
                follower_id=current_user.id,
            )
        except ObjectDoesNotExist:
            filtered_follower = None

        if filtered_follower == None:
            # new relationship
            new_following_relationship = UserFollowing(
                followed_id=hidden_user.id,
                followed_user=hidden_user,
                followed_user_settings=hidden_user_settings,
                follower_id=current_user.id,
                follower_user=current_user,
                follower_user_settings=current_user_settings,
            )
            new_following_relationship.save()
            return HttpResponseRedirect("/profile/followers/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Un-Follow form processing
    if request.POST.get("unfollow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        hidden_user = CinstagramUser.objects.get(id=hidden_user_id)
        hidden_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=hidden_user
        )
        # Check if the user already has a `follow` relationship with thecurrent
        # user, if there is not do nothing. If there is  delete  relationship
        try:
            filtered_follower = UserFollowing.objects.get(
                followed_id=hidden_user.id,
                follower_id=current_user.id,
            )
        except ObjectDoesNotExist:
            filtered_follower = None

        if filtered_follower == None:
            # do nothing since it does not exists
            pass
        else:
            # delete the relationship
            filtered_follower.delete()
            return HttpResponseRedirect("/profile/followers/")

    '''
    SELF NOTE FOR FUTURE AT THE MOMENT I AM NOT IMPLEMENTING THE + BUTTON FORM
    AT THE END OF THE PAGE FOR LOADING MORE DATA, ATM IT JUST LOADS EVERYTHING
    THE TABLE HOLDS. BUT IN THE FUTURE I WILL CHANGE IT SINCE IT IS BAD FOR
    LOADING EVERY ENTRY FROM THE DATA
    '''

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
        "accounts_following_current_user": accounts_following_current_user,
    }

    return render(request, "profile/followers.html", data)


def profile_following(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile/following.html", data)


def profile_saved(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile/saved_page.html", data)


def profile_tagged(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile/tagged_page.html", data)


# -------------------- OTHER USER PROFILES -----------------------

# ... other proflie posts, other profile followers, other profile saved ... etc.


# -------------------- Public USER PROFILES ---------------------

# only posts listing and single post page, everything else redirects to log in
