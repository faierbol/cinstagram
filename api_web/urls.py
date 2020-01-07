from django.urls import path, include
from . import views

urlpatterns = [
    # About Landing Page
    path("api_web/", views.api_web, name="about"),

    # About Job Post Listings
    path("api_web/register/", views.api_web_register, name="jobs"),

    # Specific job post
    path("api_web/post/<int:post_id>/", views.api_web_post_page, name="job_post"),

    # ...

]
