from django.urls import path, include
from . import views

urlpatterns = [
    # About Landing Page
    path("api_web/", views.api_web, name="api_web"),

    # About Job Post Listings
    path("api_web/register/", views.api_web_register, name="api_web_register"),

    # Specific job post
    path("api_web/post/<int:post_id>/", views.api_web_post_page, name="api_web_post_page"),

    # ...

]
