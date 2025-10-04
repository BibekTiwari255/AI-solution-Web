from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("solutions/", views.solutions, name="solutions"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("articles/", views.articles, name="articles"),
    path("gallery/", views.gallery, name="gallery"),
    path("events/", views.events, name="events"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
] 