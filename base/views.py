from django.shortcuts import render
from django.http import Http404

def home(request):
    """Home page view"""
    context = {
        'title': 'Home',
        'page_title': 'Welcome to Jericho Software'
    }
    return render(request, 'base/home.html', context)

def projects(request):
    """Projects listing page view"""
    projects_list = [
        {
            'slug': 'ttp-appointments',
            'name': 'TTP Appointments',
            'url': 'https://ttpappointments.com',
            'description': 'Sign up for TTP Appointment Interview Alerts and receive automatic email and text notifications for Global Entry interview appointments.',
            'featured': True,
            'logo': 'base/images/ttplogo copy.png'
        },
        {
            'slug': 'willo-decisions',
            'name': 'Willo Decisions',
            'url': 'https://willodecisions.com',
            'description': 'An interactive platform for collaborative decision-making using the Choosing By Advantages (CBA) method.',
            'featured': True,
            'logo': 'base/images/willoLogo copy.png'
        },
        {
            'slug': 'magic-dining-alerts',
            'name': 'Magic Dining Alerts',
            'url': '#',
            'description': 'A notification service for Walt Disney restaurant reservations. (Out of service)',
            'featured': False,
            'logo': 'base/images/logo copy.png'
        },
        {
            'slug': 'bible-app',
            'name': 'Bible App',
            'url': '#',
            'description': 'A comprehensive Bible application for reading, studying, and exploring scripture.',
            'featured': False,
            'logo': None
        }
    ]
    context = {
        'title': 'Projects',
        'page_title': 'My Projects',
        'projects': projects_list
    }
    return render(request, 'base/projects.html', context)

def project_detail(request, project_slug):
    """Individual project detail page view"""
    projects_data = {
        'ttp-appointments': {
            'name': 'TTP Appointments',
            'url': 'https://ttpappointments.com',
            'logo': 'base/images/ttplogo copy.png',
            'tagline': 'Sign Up Now for TTP Appointment Interview Alerts',
            'description': 'Sign up now for TTP Appointment Interview Alerts and receive automatic email and text notifications as soon as Global Entry interview appointment slots become available. Stay ahead with our Trusted Traveler Program alerts and never miss your chance to secure a Global Entry appointment.',
            'features': [
                'Free Alert with No Credit Card and No Charges',
                'One Month of Alerts, No Recurring Charges',
                'Email and Text Message Alerts',
                'Auto-reactivating Alerts',
                'Custom Date Range',
                '100% satisfaction guaranteed or your money back'
            ],
            'pricing': {
                'free': {
                    'price': 'FREE',
                    'features': [
                        'Choose up to 1 enrollment center',
                        'All enrollment centers supported',
                        'Maximum of 3 Email Alerts',
                        'No credit card required',
                        'Upgrade Anytime'
                    ]
                },
                'paid': {
                    'price': '$24.99',
                    'features': [
                        'Choose up to 5 enrollment centers',
                        'All enrollment centers supported',
                        'Unlimited Alerts',
                        'Email Alerts',
                        'Text Message Alerts',
                        'Auto-reactivating Alerts',
                        'Custom Date Range',
                        'No recurring payments',
                        '100% satisfaction guaranteed or your money back'
                    ]
                }
            },
            'how_it_works': [
                'TTP Appointments searches 24/7 automatically',
                'Receive notifications by email and text when an interview appointment becomes available',
                'Create an alert for your wanted appointment',
                'Secure your appointment interview directly on the Trusted Traveler Program website'
            ],
            'faqs': [
                {
                    'question': 'How does TTP Appointments work?',
                    'answer': 'TTP Appointments searches 24/7 automatically and will send you notifications by email and text when an interview appointment becomes available. To get notified, you need to create an alert for the wanted appointment. You will then secure your appointment interview directly on the Trusted Traveler Program website. For the free plan, you will receive up to 3 email alerts.'
                },
                {
                    'question': 'Am I guaranteed to get an appointment interview at the enrollment center I choose?',
                    'answer': 'No, TTP Appointments cannot guarantee that. We promise to use our service and check every 5 minutes for openings and notify you by email and text when there is an opening. Even if you get the notification, another person may book that slot before you reserve it.'
                },
                {
                    'question': 'Will the Alert book my appointment interview?',
                    'answer': 'No, the alert does not book your appointment interview. After you receive an alert, it is up to you to make the appointment.'
                },
                {
                    'question': 'Are you affiliated with the US Government or the Trusted Traveler Program?',
                    'answer': 'No, we are not in any way affiliated with the US Government or the Trusted Traveler Program. We just provide a service to make sure you can secure hard to get interview appointments.'
                }
            ],
            'featured_in': ['The Points Guy', 'Patch News', 'Livermore Independent']
        },
        'willo-decisions': {
            'name': 'Willo Decisions',
            'url': 'https://willodecisions.com',
            'logo': 'base/images/willoLogo copy.png',
            'tagline': 'Sharpen thinking. Simplify deciding. Rest easy.',
            'description': 'Willo provides an interactive platform for collaborative decision-making, utilizing the Choosing By Advantages (CBA) method to prioritize the most significant advantages of each option. Users can create projects, invite collaborators, and visualize decision-making through interactive charts and graphs.',
            'features': [
                'Interactive platform for collaborative decision-making',
                'Choosing By Advantages (CBA) method',
                'Create projects and invite collaborators',
                'Visualize decisions through interactive charts and graphs',
                'Customize factors and options',
                'Unlimited collaborators',
                'Adjust decisions at any time'
            ],
            'how_it_works': [
                'Create a project with your decision factors and options',
                'Invite collaborators by email',
                'Use the CBA method to identify and compare qualitative advantages',
                'Visualize the decision-making process through interactive charts',
                'Adjust rankings and decisions as needed'
            ],
            'faqs': [
                {
                    'question': 'How does Willo work?',
                    'answer': 'Willo provides an interactive platform for collaborative decision-making, utilizing the Choosing By Advantages (CBA) method to prioritize the most significant advantages of each option. Users can create projects, invite collaborators, and visualize decision-making through interactive charts and graphs.'
                },
                {
                    'question': 'What is the Choosing By Advantages (CBA) method?',
                    'answer': 'The CBA method focuses on identifying and comparing the qualitative advantages of each option rather than relying solely on numerical scores. This approach ensures that decisions are based on the actual benefits and trade-offs of each option, leading to more informed and effective outcomes.'
                },
                {
                    'question': 'How can I invite collaborators to my project?',
                    'answer': 'You can invite collaborators to your project by adding their email addresses in the project settings. Invited collaborators can join once you give them the project link, then they can join the project and contribute to the decision-making process.'
                },
                {
                    'question': 'What makes Willo different from other decision matrices?',
                    'answer': 'Willo stands out due to its unique implementation of the Choosing By Advantages (CBA) method. Unlike traditional decision matrices that often rely solely on numerical scores and weights, CBA focuses on the qualitative advantages of each option. This approach ensures more informed and effective outcomes by considering the actual benefits and trade-offs of each option.'
                },
                {
                    'question': 'Can I change my decisions after submitting them?',
                    'answer': 'Yes, you can go back and adjust your decisions at any time. Willo allows you to revisit previous steps, modify your rankings, and update your project as needed to ensure the best possible outcomes.'
                },
                {
                    'question': 'Is there a limit to the number of collaborators I can invite?',
                    'answer': 'No, there is no limit to the number of collaborators you can invite to your project. You can include as many team members as needed to ensure a comprehensive evaluation of all factors and options.'
                }
            ]
        },
        'magic-dining-alerts': {
            'name': 'Magic Dining Alerts',
            'url': '#',
            'logo': 'base/images/logo copy.png',
            'tagline': 'Notification Service for Walt Disney Restaurant Reservations',
            'description': 'Magic Dining Alerts was a notification service designed to help users secure hard-to-get Walt Disney restaurant reservations. The service sent alerts when dining reservations became available.',
            'features': [
                'Email and SMS notifications',
                'Real-time reservation alerts',
                'Multiple restaurant monitoring',
                'Easy sign-up process'
            ],
            'how_it_works': [
                'Users signed up for alerts on specific Disney restaurants',
                'The service monitored reservation availability',
                'Users received notifications when reservations opened',
                'Users could then book directly through Disney\'s system'
            ],
            'faqs': [
                {
                    'question': 'Is Magic Dining Alerts still available?',
                    'answer': 'No, Magic Dining Alerts is currently out of service.'
                }
            ],
            'out_of_service': True
        },
        'bible-app': {
            'name': 'Bible App',
            'url': '#',
            'logo': None,
            'tagline': 'Read, Study, and Explore Scripture',
            'description': 'A comprehensive Bible application designed to help you read, study, and explore scripture. This app provides an intuitive interface for accessing the Bible, with features designed to enhance your study and understanding of God\'s word.',
            'features': [
                'Complete Bible text in multiple translations',
                'Reading plans and devotionals',
                'Bookmark and highlight verses',
                'Search functionality',
                'Notes and annotations',
                'Offline access',
                'Cross-references and study tools'
            ],
            'how_it_works': [
                'Download and install the app',
                'Choose your preferred Bible translation',
                'Navigate through books, chapters, and verses',
                'Use study tools to deepen your understanding',
                'Save your favorite verses and create notes'
            ],
            'faqs': [
                {
                    'question': 'What Bible translations are available?',
                    'answer': 'The app includes multiple popular Bible translations. More details coming soon as the app is finalized.'
                },
                {
                    'question': 'Can I use the app offline?',
                    'answer': 'Yes, once you download the Bible text, you can access it offline without an internet connection.'
                },
                {
                    'question': 'Is the app free?',
                    'answer': 'Details about pricing and availability will be announced soon. Stay tuned for updates!'
                }
            ],
            'coming_soon': True
        }
    }
    
    # Validate project_slug to prevent potential issues
    if not project_slug or not isinstance(project_slug, str):
        raise Http404("Invalid project identifier")
    
    project = projects_data.get(project_slug)
    if not project:
        raise Http404(f"Project '{project_slug}' not found. Please check the URL and try again.")
    
    context = {
        'title': project['name'],
        'page_title': project['name'],
        'project': project
    }
    return render(request, 'base/project_detail.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About',
        'page_title': 'About Me'
    }
    return render(request, 'base/about.html', context)

def privacy_policy(request):
    """Privacy Policy page view"""
    context = {
        'title': 'Privacy Policy',
        'page_title': 'Privacy Policy'
    }
    return render(request, 'base/privacy_policy.html', context)

def custom_404(request, exception):
    """Custom 404 error handler"""
    context = {
        'title': '404 - Page Not Found',
        'page_title': 'Page Not Found'
    }
    return render(request, 'base/404.html', context, status=404)

def custom_500(request):
    """Custom 500 error handler"""
    context = {
        'title': '500 - Server Error',
        'page_title': 'Server Error'
    }
    return render(request, 'base/500.html', context, status=500)
