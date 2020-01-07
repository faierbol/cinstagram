# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports


def api_web(request):
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "", data)


def api_web_register(request):
    # Deleting any sessions regarding top-tier type of users

    data = {

    }
    return render(request, "about/job_postings.html", data)


def api_web_post_page(request, job_id):
    # Deleting any sessions regarding top-tier type of users

    data = {

    }
    return render(request, "about/jobs_post_page.html", data)
