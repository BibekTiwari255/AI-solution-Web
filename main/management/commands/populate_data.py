from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from main.models import (
    Solution, Event, Article, GalleryImage, Testimonial, PricingPlan
)


class Command(BaseCommand):
    help = 'Populate the database with sample data for all models'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create Solutions
        self.create_solutions()
        
        # Create Events
        self.create_events()
        
        # Create Articles
        self.create_articles()
        
        # Create Testimonials
        self.create_testimonials()
        
        # Create Pricing Plans
        self.create_pricing_plans()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )

    def create_solutions(self):
        solutions_data = [
            {
                'title': 'AI Virtual Assistant',
                'description': 'Transform your customer service and internal operations with our intelligent virtual assistant that understands context, learns from interactions, and provides instant, accurate responses.',
                'category': 'ai_assistant',
                'features': [
                    'Natural language processing',
                    'Multi-channel integration',
                    'Custom knowledge base',
                    'Analytics dashboard'
                ],
                'metrics': {'resolution': '80%', 'availability': '24/7'},
                'pricing': 2999.00,
                'is_featured': True,
            },
            {
                'title': 'Rapid Prototyping',
                'description': 'Validate your AI concepts quickly with our rapid prototyping service. We help you build, test, and iterate on AI solutions in record time.',
                'category': 'rapid_prototyping',
                'features': [
                    'Quick concept validation',
                    'Interactive demos',
                    'Technical feasibility',
                    'Cost estimation'
                ],
                'metrics': {'initial_prototype': '48h', 'full_mvp': '2w'},
                'pricing': 1999.00,
                'is_featured': True,
            },
            {
                'title': 'Service Desk Assistant',
                'description': 'Automate FAQs, triage tickets, and provide instant support with our intelligent service desk solution.',
                'category': 'ai_assistant',
                'features': [
                    'Instant responses',
                    'Smart ticket routing',
                    'Performance analytics'
                ],
                'metrics': {'response_time': '< 2s', 'accuracy': '95%'},
                'pricing': 1999.00,
            },
            {
                'title': 'DevOps Copilot',
                'description': 'AI-powered DevOps assistant that provides alerts, automated remediations, and deployment guidance.',
                'category': 'automation',
                'features': [
                    'Smart alerts',
                    'Auto remediation',
                    'Deployment guidance'
                ],
                'metrics': {'uptime': '99.9%', 'incidents': '-60%'},
                'pricing': 3999.00,
            },
            {
                'title': 'UX Insights',
                'description': 'Detect friction in workflows and get AI-powered recommendations to improve user experience.',
                'category': 'analytics',
                'features': [
                    'Friction detection',
                    'Smart recommendations',
                    'Usage analytics'
                ],
                'metrics': {'improvement': '40%', 'satisfaction': '+25%'},
                'pricing': 2499.00,
            },
            {
                'title': 'Smart Data Analytics',
                'description': 'Transform raw data into actionable insights with AI-powered analytics and automated reporting.',
                'category': 'data',
                'features': [
                    'Automated reports',
                    'Visual dashboards',
                    'Predictive insights'
                ],
                'metrics': {'processing': '10x faster', 'accuracy': '98%'},
                'pricing': 3499.00,
            },
            {
                'title': 'AI Security Monitor',
                'description': 'Advanced threat detection and automated security monitoring powered by machine learning.',
                'category': 'security',
                'features': [
                    'Threat detection',
                    'Automated response',
                    'Compliance reports'
                ],
                'metrics': {'threats_detected': '99.5%', 'response_time': '< 1min'},
                'pricing': 4999.00,
            },
            {
                'title': 'Workflow Automation',
                'description': 'Streamline business processes with intelligent workflow automation and smart decision making.',
                'category': 'automation',
                'features': [
                    'Process automation',
                    'Smart decisions',
                    'Easy configuration'
                ],
                'metrics': {'efficiency': '+50%', 'errors': '-80%'},
                'pricing': 2799.00,
            },
        ]
        
        for data in solutions_data:
            Solution.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
        
        self.stdout.write(f'Created {len(solutions_data)} solutions')

    def create_events(self):
        base_date = timezone.now() + timedelta(days=30)
        
        events_data = [
            {
                'title': 'AI Solutions Summit 2025: The Future of Digital Employee Experience',
                'description': 'Join industry leaders, AI experts, and digital transformation specialists for a comprehensive exploration of how artificial intelligence is reshaping the modern workplace.',
                'event_type': 'conference',
                'date': base_date + timedelta(days=45),
                'location': 'Sunderland, UK',
                'duration': '2 Days',
                'price': 'Free',
                'spots_remaining': 150,
                'is_featured': True,
            },
            {
                'title': 'Rapid AI Prototyping Workshop',
                'description': 'Hands-on session where you\'ll learn to build and deploy AI prototypes in just 4 hours. Perfect for product managers and developers.',
                'event_type': 'workshop',
                'date': base_date + timedelta(days=20),
                'location': 'AI-Solutions Office, Sunderland',
                'duration': '4 hours',
                'price': 'Free',
                'spots_remaining': 12,
            },
            {
                'title': 'Global AI Implementation Strategies',
                'description': 'Learn how to scale AI solutions across international teams and navigate regulatory requirements in different markets.',
                'event_type': 'webinar',
                'date': base_date + timedelta(days=28),
                'location': 'Online Event',
                'duration': '1.5 hours',
                'price': 'Free',
                'spots_remaining': None,
            },
            {
                'title': 'AI Security & Compliance Summit',
                'description': 'Deep dive into enterprise AI security, data privacy regulations, and compliance frameworks for AI implementations.',
                'event_type': 'conference',
                'date': base_date + timedelta(days=38),
                'location': 'London, UK',
                'duration': '8 hours',
                'price': '£299',
                'spots_remaining': 45,
            },
            {
                'title': 'AI Solutions User Meetup',
                'description': 'Connect with other AI Solutions users, share experiences, and learn about new features and best practices.',
                'event_type': 'networking',
                'date': base_date + timedelta(days=42),
                'location': 'Newcastle, UK',
                'duration': '2 hours',
                'price': 'Free',
                'spots_remaining': 28,
            },
            {
                'title': 'Measuring AI ROI & Impact',
                'description': 'Learn how to measure and communicate the business impact of your AI initiatives with concrete metrics and case studies.',
                'event_type': 'masterclass',
                'date': base_date + timedelta(days=52),
                'location': 'Manchester, UK',
                'duration': '6 hours',
                'price': '£199',
                'spots_remaining': 18,
            },
            {
                'title': 'AI Solutions Product Demo',
                'description': 'See our latest AI features in action and get hands-on experience with our virtual assistant and prototyping tools.',
                'event_type': 'demo',
                'date': base_date + timedelta(days=65),
                'location': 'AI-Solutions Office, Sunderland',
                'duration': '2 hours',
                'price': 'Free',
                'spots_remaining': 25,
            },
        ]
        
        for data in events_data:
            Event.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
        
        self.stdout.write(f'Created {len(events_data)} events')

    def create_articles(self):
        articles_data = [
            {
                'title': 'The Future of Digital Employee Experience: How AI is Transforming the Workplace',
                'slug': 'future-digital-employee-experience-ai-transforming-workplace',
                'description': 'Discover how artificial intelligence is revolutionizing the way employees interact with technology, boosting productivity, and creating more intuitive digital experiences across organizations.',
                'content': 'Full article content would go here...',
                'category': 'ai',
                'read_time': 5,
                'author': 'AI-Solutions Team',
                'views': 2300,
                'is_featured': True,
            },
            {
                'title': 'Building AI-Powered Virtual Assistants for Enterprise',
                'slug': 'building-ai-powered-virtual-assistants-enterprise',
                'description': 'Learn how to design and implement intelligent virtual assistants that can handle complex employee queries and streamline internal processes.',
                'content': 'Full article content would go here...',
                'category': 'ai',
                'read_time': 4,
                'author': 'AI-Solutions Team',
                'views': 1800,
            },
            {
                'title': 'Rapid Prototyping: From Idea to Implementation in 48 Hours',
                'slug': 'rapid-prototyping-idea-implementation-48-hours',
                'description': 'Discover our proven methodology for creating functional AI prototypes that validate ideas quickly and cost-effectively.',
                'content': 'Full article content would go here...',
                'category': 'prototyping',
                'read_time': 6,
                'author': 'AI-Solutions Team',
                'views': 1500,
            },
            {
                'title': 'Measuring Digital Employee Experience: Key Metrics That Matter',
                'slug': 'measuring-digital-employee-experience-key-metrics',
                'description': 'Understand which metrics to track and how to measure the success of your digital employee experience initiatives.',
                'content': 'Full article content would go here...',
                'category': 'analytics',
                'read_time': 5,
                'author': 'AI-Solutions Team',
                'views': 1200,
            },
            {
                'title': 'Enterprise AI Security: Best Practices for Data Protection',
                'slug': 'enterprise-ai-security-best-practices-data-protection',
                'description': 'Essential security considerations when implementing AI solutions in enterprise environments, including data privacy and compliance.',
                'content': 'Full article content would go here...',
                'category': 'security',
                'read_time': 7,
                'author': 'AI-Solutions Team',
                'views': 900,
            },
            {
                'title': 'Seamless AI Integration: Connecting Your Existing Tools',
                'slug': 'seamless-ai-integration-connecting-existing-tools',
                'description': 'Learn how to integrate AI solutions with your current tech stack without disrupting existing workflows.',
                'content': 'Full article content would go here...',
                'category': 'integration',
                'read_time': 4,
                'author': 'AI-Solutions Team',
                'views': 1100,
            },
            {
                'title': 'Scaling AI Solutions Across Global Teams',
                'slug': 'scaling-ai-solutions-across-global-teams',
                'description': 'Strategies for deploying AI-powered tools across different time zones, cultures, and regulatory environments.',
                'content': 'Full article content would go here...',
                'category': 'global',
                'read_time': 6,
                'author': 'AI-Solutions Team',
                'views': 800,
            },
        ]
        
        for data in articles_data:
            Article.objects.get_or_create(
                slug=data['slug'],
                defaults=data
            )
        
        self.stdout.write(f'Created {len(articles_data)} articles')

    def create_testimonials(self):
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'position': 'CTO',
                'company': 'TechCorp Solutions',
                'industry': 'technology',
                'content': 'AI-Solutions transformed our customer service operations. The virtual assistant handles 80% of queries automatically, freeing up our team to focus on complex issues.',
                'rating': 5,
                'avatar_initials': 'SJ',
                'is_featured': True,
            },
            {
                'name': 'Michael Chen',
                'position': 'Operations Director',
                'company': 'HealthFirst Medical',
                'industry': 'healthcare',
                'content': 'The rapid prototyping service helped us validate our AI concept in just 48 hours. Incredible speed and quality of work.',
                'rating': 5,
                'avatar_initials': 'MC',
                'is_featured': True,
            },
            {
                'name': 'Emma Williams',
                'position': 'Head of Digital',
                'company': 'RetailMax',
                'industry': 'retail',
                'content': 'Our employee productivity increased by 40% after implementing their workflow automation solution. Highly recommended!',
                'rating': 5,
                'avatar_initials': 'EW',
                'is_featured': True,
            },
            {
                'name': 'David Rodriguez',
                'position': 'IT Director',
                'company': 'Manufacturing Plus',
                'industry': 'manufacturing',
                'content': 'The AI security monitoring has been a game-changer. We\'ve detected and prevented 99.5% of potential threats automatically.',
                'rating': 4,
                'avatar_initials': 'DR',
            },
            {
                'name': 'Lisa Thompson',
                'position': 'VP of Operations',
                'company': 'FinanceFirst',
                'industry': 'financial',
                'content': 'Outstanding analytics and insights. The data visualization tools help us make better decisions faster.',
                'rating': 5,
                'avatar_initials': 'LT',
            },
            {
                'name': 'James Wilson',
                'position': 'Chief Innovation Officer',
                'company': 'EduTech Solutions',
                'industry': 'education',
                'content': 'The AI integration was seamless. Our existing systems work perfectly with their solutions.',
                'rating': 4,
                'avatar_initials': 'JW',
            },
        ]
        
        for data in testimonials_data:
            Testimonial.objects.get_or_create(
                name=data['name'],
                company=data['company'],
                defaults=data
            )
        
        self.stdout.write(f'Created {len(testimonials_data)} testimonials')

    def create_pricing_plans(self):
        pricing_plans_data = [
            {
                'name': 'Starter',
                'price': '£2,999',
                'period': 'per month',
                'description': 'Perfect for small teams getting started with AI',
                'features': [
                    '1 AI Virtual Assistant',
                    'Basic analytics',
                    'Email support',
                    'Standard integrations'
                ],
                'is_popular': False,
            },
            {
                'name': 'Professional',
                'price': '£7,999',
                'period': 'per month',
                'description': 'Most popular choice for growing businesses',
                'features': [
                    '3 AI Solutions',
                    'Advanced analytics',
                    'Priority support',
                    'Custom integrations',
                    'Rapid prototyping'
                ],
                'is_popular': True,
            },
            {
                'name': 'Enterprise',
                'price': 'Custom',
                'period': 'contact us',
                'description': 'Tailored solutions for large organizations',
                'features': [
                    'Unlimited solutions',
                    'Full analytics suite',
                    '24/7 dedicated support',
                    'Custom development',
                    'On-premise deployment'
                ],
                'is_popular': False,
            },
        ]
        
        for data in pricing_plans_data:
            PricingPlan.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
        
        self.stdout.write(f'Created {len(pricing_plans_data)} pricing plans')
