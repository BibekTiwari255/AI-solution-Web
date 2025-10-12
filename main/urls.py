from django.urls import path
from . import views
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test view is working! Django is running correctly.")

urlpatterns = [
    path("test/", test_view, name="test"),
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