from django.contrib import admin
from .models import (
    Inquiry, Solution, Event, Article, GalleryImage, 
    Testimonial, PricingPlan
)


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "company_name", "country", "created_at")
    search_fields = ("full_name", "email", "company_name", "country", "job_title")
    list_filter = ("country", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "is_active", "created_at")
    list_filter = ("category", "is_featured", "is_active", "created_at")
    search_fields = ("title", "description")
    list_editable = ("is_featured", "is_active")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_type", "date", "location", "price", "is_featured", "is_active")
    list_filter = ("event_type", "is_featured", "is_active", "date")
    search_fields = ("title", "description", "location")
    list_editable = ("is_featured", "is_active")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "date"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "is_featured", "is_published", "published_at")
    list_filter = ("category", "is_featured", "is_published", "published_at")
    search_fields = ("title", "description", "content", "author")
    list_editable = ("is_featured", "is_published")
    readonly_fields = ("created_at", "updated_at", "views")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "alt_text")
    readonly_fields = ("created_at","updated_at")   


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "industry", "rating", "is_featured", "is_active")
    list_filter = ("industry", "rating", "is_featured", "is_active", "created_at")
    search_fields = ("name", "company", "position", "content")
    list_editable = ("is_featured", "is_active")
    readonly_fields = ("created_at", "updated_at")


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "period", "is_popular", "is_active")
    list_filter = ("is_popular", "is_active", "created_at")
    search_fields = ("name", "description")
    list_editable = ("is_popular", "is_active")
    readonly_fields = ("created_at", "updated_at")
