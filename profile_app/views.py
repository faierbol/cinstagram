# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports


def profile_posts_page(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile/posts_page.html", data)


def profile_single_post_page(request, post_id):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile/post_page.html", data)


def profile_post_likers(request, post_id):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "profile/likers.html", data)


def profile_followers(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

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
