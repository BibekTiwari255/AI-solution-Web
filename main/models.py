from django.db import models
from django.utils import timezone

# Create your models here.


class Inquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=120, blank=True)
    job_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.full_name} - {self.email}"


class Solution(models.Model):
    CATEGORY_CHOICES = [
        ('ai_assistant', 'AI Virtual Assistant'),
        ('rapid_prototyping', 'Rapid Prototyping'),
        ('analytics', 'Analytics & Insights'),
        ('security', 'Security & Compliance'),
        ('automation', 'Workflow Automation'),
        ('data', 'Data Analytics'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='solutions/', null=True, blank=True, help_text="Solution image/icon")
    features = models.JSONField(default=list, help_text="List of features")
    metrics = models.JSONField(default=dict, help_text="Key metrics (e.g., {'resolution': '80%', 'availability': '24/7'})")
    pricing = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self) -> str:
        return self.title


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('workshop', 'Workshop'),
        ('webinar', 'Webinar'),
        ('conference', 'Conference'),
        ('networking', 'Networking'),
        ('demo', 'Demo Day'),
        ('masterclass', 'Masterclass'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    image = models.ImageField(upload_to='events/', null=True, blank=True, help_text="Event image/icon")
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    duration = models.CharField(max_length=100, help_text="e.g., '2 Days', '4 hours'")
    price = models.CharField(max_length=50, default="Free")
    spots_remaining = models.PositiveIntegerField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date"]

    def __str__(self) -> str:
        return f"{self.title} - {self.date.strftime('%B %d, %Y')}"


class Article(models.Model):
    CATEGORY_CHOICES = [
        ('ai', 'AI & Machine Learning'),
        ('prototyping', 'Rapid Prototyping'),
        ('analytics', 'Analytics & Insights'),
        ('security', 'Security & Compliance'),
        ('integration', 'Integration'),
        ('global', 'Global'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of title")
    description = models.TextField()
    content = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='articles/', null=True, blank=True, help_text="Article featured image")
    read_time = models.PositiveIntegerField(help_text="Reading time in minutes")
    author = models.CharField(max_length=100, default="AI-Solutions Team")
    views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self) -> str:
        return self.title


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('events', 'Events'),
        ('office', 'Office'),
        ('team', 'Team'),
        ('products', 'Products'),
        ('conferences', 'Conferences'),
        ('workshops', 'Workshops'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery/')
    alt_text = models.CharField(max_length=200, help_text="Alternative text for accessibility")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self) -> str:
        return self.title


class Testimonial(models.Model):
    INDUSTRY_CHOICES = [
        ('healthcare', 'Healthcare'),
        ('retail', 'Retail'),
        ('manufacturing', 'Manufacturing'),
        ('financial', 'Financial'),
        ('education', 'Education'),
        ('technology', 'Technology'),
        ('logistics', 'Logistics'),
    ]
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    content = models.TextField()
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    avatar_initials = models.CharField(max_length=2, help_text="Initials for avatar (e.g., 'SJ')")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self) -> str:
        return f"{self.name} - {self.company}"


class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50, help_text="e.g., '£2,999', 'Custom'")
    period = models.CharField(max_length=50, default="per month")
    description = models.TextField(blank=True)
    features = models.JSONField(default=list, help_text="List of features")
    is_popular = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["price"]

    def __str__(self) -> str:
        return self.name
