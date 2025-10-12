from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import models, connection
from django.core.exceptions import ImproperlyConfigured
import logging

from .forms import ContactForm
from .models import (
    Inquiry, Solution, Event, Article, GalleryImage, 
    Testimonial, PricingPlan
)

logger = logging.getLogger(__name__)


def safe_query(model_class, **filters):
    """Safely query database models with error handling"""
    try:
        return model_class.objects.filter(**filters)
    except Exception as e:
        logger.error(f"Database error in {model_class.__name__}: {str(e)}")
        return model_class.objects.none()


def home(request):
    return render(request, "main/home.html")


def solutions(request):
    try:
        solutions = safe_query(Solution, is_active=True)
        featured_solutions = solutions.filter(is_featured=True)
        pricing_plans = safe_query(PricingPlan, is_active=True)
        
        context = {
            'solutions': solutions,
            'featured_solutions': featured_solutions,
            'pricing_plans': pricing_plans,
        }
        return render(request, "main/solutions.html", context)
    except Exception as e:
        logger.error(f"Error in solutions view: {str(e)}")
        return render(request, "main/solutions.html", {
            'solutions': Solution.objects.none(),
            'featured_solutions': Solution.objects.none(),
            'pricing_plans': PricingPlan.objects.none(),
        })


def portfolio(request):
    return render(request, "main/portfolio.html")


def testimonials(request):
    try:
        testimonials = safe_query(Testimonial, is_active=True)
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
    except Exception as e:
        logger.error(f"Error in testimonials view: {str(e)}")
        return render(request, "main/testimonials.html", {
            'testimonials': Testimonial.objects.none(),
            'featured_testimonials': Testimonial.objects.none(),
            'industry_stats': {},
        })


def articles(request):
    try:
        articles = safe_query(Article, is_published=True)
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
    except Exception as e:
        logger.error(f"Error in articles view: {str(e)}")
        return render(request, "main/articles.html", {
            'articles': Article.objects.none(),
            'featured_articles': Article.objects.none(),
            'category_stats': {},
        })


def gallery(request):
    try:
        images = safe_query(GalleryImage, is_active=True)
        featured_images = images.filter(is_featured=True)
        
        context = {
            "images": images,
            "title": "Photo Gallery",  # 👈 Pass title here
            "subtitle": "Promotional events and moments.",
            "icon_class": "ri-gallery-line",
        }
        return render(request, "main/gallery.html", context)
    except Exception as e:
        logger.error(f"Error in gallery view: {str(e)}")
        return render(request, "main/gallery.html", {
            "images": GalleryImage.objects.none(),
            "title": "Photo Gallery",
            "subtitle": "Promotional events and moments.",
            "icon_class": "ri-gallery-line",
        })


def events(request):
    try:
        events = safe_query(Event, is_active=True)
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
    except Exception as e:
        logger.error(f"Error in events view: {str(e)}")
        return render(request, "main/events.html", {
            'events': Event.objects.none(),
            'featured_events': Event.objects.none(),
            'event_type_stats': {},
        })


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
    try:
        total_inquiries = Inquiry.objects.count()
        recent_inquiries = Inquiry.objects.all()[:10]
        return render(
            request,
            "main/admin_dashboard.html",
            {"total_inquiries": total_inquiries, "recent_inquiries": recent_inquiries},
        )
    except Exception as e:
        logger.error(f"Error in admin_dashboard view: {str(e)}")
        return render(
            request,
            "main/admin_dashboard.html",
            {"total_inquiries": 0, "recent_inquiries": Inquiry.objects.none()},
        )
