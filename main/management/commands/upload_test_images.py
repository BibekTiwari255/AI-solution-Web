from django.core.management.base import BaseCommand
from PIL import Image
import os
from main.models import Solution, Event, Article

class Command(BaseCommand):
    help = 'Create test images for solutions, events, and articles'

    def handle(self, *args, **options):
        self.stdout.write('Creating test images...')
        
        # Create test images for solutions
        self.create_solution_images()
        
        # Create test images for events
        self.create_event_images()
        
        # Create test images for articles
        self.create_article_images()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created test images!')
        )

    def create_solution_images(self):
        """Create test images for solutions"""
        colors = [
            ('red', 'AI Virtual Assistant'),
            ('blue', 'Rapid Prototyping'),
            ('green', 'Service Desk Assistant'),
            ('purple', 'DevOps Copilot'),
            ('orange', 'UX Insights'),
            ('teal', 'Smart Data Analytics'),
            ('pink', 'AI Security Monitor'),
            ('indigo', 'Workflow Automation'),
        ]
        
        solutions = Solution.objects.all()
        for i, solution in enumerate(solutions):
            if i < len(colors):
                color, title = colors[i]
                img = Image.new('RGB', (200, 200), color=color)
                
                # Add text to image
                from PIL import ImageDraw, ImageFont
                draw = ImageDraw.Draw(img)
                
                # Try to use a default font, fallback to basic if not available
                try:
                    font = ImageFont.truetype("arial.ttf", 20)
                except:
                    font = ImageFont.load_default()
                
                # Draw title
                text_bbox = draw.textbbox((0, 0), title, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                
                x = (200 - text_width) // 2
                y = (200 - text_height) // 2
                
                draw.text((x, y), title, fill='white', font=font)
                
                # Save image
                filename = f'solutions/solution_{solution.id}_{color}.png'
                img.save(f'media/{filename}')
                
                # Update solution
                solution.image = filename
                solution.save()
                
                self.stdout.write(f'Created image for {solution.title}')

    def create_event_images(self):
        """Create test images for events"""
        colors = [
            ('red', 'Conference'),
            ('blue', 'Workshop'),
            ('green', 'Webinar'),
            ('purple', 'Networking'),
            ('orange', 'Masterclass'),
            ('teal', 'Demo'),
        ]
        
        events = Event.objects.all()
        for i, event in enumerate(events):
            if i < len(colors):
                color, event_type = colors[i]
                img = Image.new('RGB', (200, 200), color=color)
                
                # Add text to image
                from PIL import ImageDraw, ImageFont
                draw = ImageDraw.Draw(img)
                
                try:
                    font = ImageFont.truetype("arial.ttf", 16)
                except:
                    font = ImageFont.load_default()
                
                # Draw event type
                text_bbox = draw.textbbox((0, 0), event_type, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                
                x = (200 - text_width) // 2
                y = (200 - text_height) // 2
                
                draw.text((x, y), event_type, fill='white', font=font)
                
                # Save image
                filename = f'events/event_{event.id}_{color}.png'
                img.save(f'media/{filename}')
                
                # Update event
                event.image = filename
                event.save()
                
                self.stdout.write(f'Created image for {event.title}')

    def create_article_images(self):
        """Create test images for articles"""
        colors = [
            ('red', 'AI'),
            ('blue', 'Prototyping'),
            ('green', 'Analytics'),
            ('purple', 'Security'),
            ('orange', 'Integration'),
            ('teal', 'Global'),
        ]
        
        articles = Article.objects.all()
        for i, article in enumerate(articles):
            if i < len(colors):
                color, category = colors[i]
                img = Image.new('RGB', (200, 200), color=color)
                
                # Add text to image
                from PIL import ImageDraw, ImageFont
                draw = ImageDraw.Draw(img)
                
                try:
                    font = ImageFont.truetype("arial.ttf", 18)
                except:
                    font = ImageFont.load_default()
                
                # Draw category
                text_bbox = draw.textbbox((0, 0), category, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                
                x = (200 - text_width) // 2
                y = (200 - text_height) // 2
                
                draw.text((x, y), category, fill='white', font=font)
                
                # Save image
                filename = f'articles/article_{article.id}_{color}.png'
                img.save(f'media/{filename}')
                
                # Update article
                article.image = filename
                article.save()
                
                self.stdout.write(f'Created image for {article.title}')
