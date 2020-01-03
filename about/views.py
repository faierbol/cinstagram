# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports


def about(request):

    data = {

    }

    return render(request, "about/about_index.html", data)


def jobs(request):
    return HttpResponse("about -- jobs")


def job_post(request, job_id):
    return HttpResponse("about -- job post")


def legal(request):
    return HttpResponse("about -- legal")
