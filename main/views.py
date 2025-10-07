from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from django.db.models import Avg, Count

from .forms import ContactForm
from .models import (
    Inquiry, Solution, Event, Article, GalleryImage,
    Testimonial, PricingPlan
)


def home(request):
    return render(request, "main/home.html")


def solutions(request):
    solutions_qs = Solution.objects.filter(is_active=True)
    context = {
        "solutions": solutions_qs,
        "featured_solutions": solutions_qs.filter(is_featured=True),
        "pricing_plans": PricingPlan.objects.all()
    }
    return render(request, "main/solutions.html", context)


def portfolio(request):
    return render(request, "main/portfolio.html")


def testimonials(request):
    testimonials_qs = Testimonial.objects.filter(is_active=True)

    # Industry stats in one query
    industry_agg = (
        testimonials_qs.values("industry")
        .annotate(count=Count("id"), avg_rating=Avg("rating"))
    )

    # Convert to simple dict with rounded avg
    industry_stats = {
        row["industry"]: {
            "count": row["count"],
            "avg_rating": round(row["avg_rating"] or 0, 1),
        }
        for row in industry_agg
        if row["count"] > 0
    }

    context = {
        "testimonials": testimonials_qs,
        "featured_testimonials": testimonials_qs.filter(is_featured=True),
        "industry_stats": industry_stats,
    }
    return render(request, "main/testimonials.html", context)


def articles(request):
    articles_qs = Article.objects.filter(is_published=True)

    # Category stats in one query
    category_stats = {
        row["category"]: row["count"]
        for row in articles_qs.values("category").annotate(count=Count("id"))
        if row["count"] > 0
    }

    context = {
        "articles": articles_qs,
        "featured_articles": articles_qs.filter(is_featured=True),
        "category_stats": category_stats,
    }
    return render(request, "main/articles.html", context)


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, "main/gallery.html", {"images": images})


def events(request):
    events_qs = Event.objects.filter(is_active=True)
    upcoming = events_qs.filter(date__gte=timezone.now())

    # Event type stats in one query (on active events; switch to 'upcoming' if desired)
    event_type_stats = {
        row["event_type"]: row["count"]
        for row in events_qs.values("event_type").annotate(count=Count("id"))
        if row["count"] > 0
    }

    context = {
        "events": events_qs,
        "featured_events": upcoming.filter(is_featured=True),
        "event_type_stats": event_type_stats,
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
            messages.error(request, "Please fix the errors below.")
    else:
        form = ContactForm()
    return render(request, "main/contact.html", {"form": form})


@login_required
def admin_dashboard(request):
    total_inquiries = Inquiry.objects.count()
    recent_inquiries = Inquiry.objects.all()[:10]  # Ordered by Meta on Inquiry
    return render(
        request,
        "main/admin_dashboard.html",
        {"total_inquiries": total_inquiries, "recent_inquiries": recent_inquiries},
    )
