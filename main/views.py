from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import models

from .forms import ContactForm
from .models import (
    Inquiry, Solution, Event, Article, GalleryImage, 
    Testimonial, PricingPlan
)


def home(request):
    return render(request, "main/home.html")


def solutions(request):
    solutions = Solution.objects.filter(is_active=True)
    featured_solutions = solutions.filter(is_featured=True)
    pricing_plans = PricingPlan.objects.filter(is_active=True)
    
    context = {
        'solutions': solutions,
        'featured_solutions': featured_solutions,
        'pricing_plans': pricing_plans,
    }
    return render(request, "main/solutions.html", context)


def portfolio(request):
    return render(request, "main/portfolio.html")


def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    featured_testimonials = testimonials.filter(is_featured=True)
    
    # Get industry statistics
    industry_stats = {}
    for industry, _ in Testimonial.INDUSTRY_CHOICES:
        count = testimonials.filter(industry=industry).count()
        if count > 0:
            avg_rating = testimonials.filter(industry=industry).aggregate(
                avg_rating=models.Avg('rating')
            )['avg_rating']
            industry_stats[industry] = {
                'count': count,
                'avg_rating': round(avg_rating, 1)
            }
    
    context = {
        'testimonials': testimonials,
        'featured_testimonials': featured_testimonials,
        'industry_stats': industry_stats,
    }
    return render(request, "main/testimonials.html", context)


def articles(request):
    articles = Article.objects.filter(is_published=True)
    featured_articles = articles.filter(is_featured=True)
    
    # Get category statistics
    category_stats = {}
    for category, _ in Article.CATEGORY_CHOICES:
        count = articles.filter(category=category).count()
        if count > 0:
            category_stats[category] = count
    
    context = {
        'articles': articles,
        'featured_articles': featured_articles,
        'category_stats': category_stats,
    }
    return render(request, "main/articles.html", context)


def gallery(request):
    images = GalleryImage.objects.filter(is_active=True)
    featured_images = images.filter(is_featured=True)
    
    context = {
        'images': images,
        'featured_images': featured_images,
    }
    return render(request, "main/gallery.html", context)


def events(request):
    events = Event.objects.filter(is_active=True)
    featured_events = events.filter(is_featured=True)
    
    # Get event type statistics
    event_type_stats = {}
    for event_type, _ in Event.EVENT_TYPE_CHOICES:
        count = events.filter(event_type=event_type).count()
        if count > 0:
            event_type_stats[event_type] = count
    
    context = {
        'events': events,
        'featured_events': featured_events,
        'event_type_stats': event_type_stats,
    }
    return render(request, "main/events.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We'll get back to you shortly.")
            return redirect(reverse("contact"))
    else:
        form = ContactForm()
    return render(request, "main/contact.html", {"form": form})


@login_required
def admin_dashboard(request):
    total_inquiries = Inquiry.objects.count()
    recent_inquiries = Inquiry.objects.all()[:10]
    return render(
        request,
        "main/admin_dashboard.html",
        {"total_inquiries": total_inquiries, "recent_inquiries": recent_inquiries},
    )
