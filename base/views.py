from django.shortcuts import render
from django.http import Http404


# Every project lives here once; the list page, detail page, home page and
# about page all read from it. Order = display order.
PROJECTS = [
    {
        'slug': 'retireplanai',
        'name': 'RetirePlanAI',
        'url': 'https://retireplanai.com',
        'logo': 'base/images/retireplanai-logo.png',
        'status': 'Live',
        'featured': True,
        'summary': 'Retirement planning software with Monte Carlo simulations, tax-aware projections and an AI coach you can talk to about your plan.',
        'tagline': 'Plan your retirement with confidence, before you retire.',
        'stack': ['Django', 'Python', 'Stripe', 'MCP'],
        'description': [
            'RetirePlanAI started while I was helping family members work through real retirement decisions. The tools we found were either too simple to trust or too opaque to understand, so I built one that shows its work.',
            'You enter your accounts, income, spending and goals once, and it projects your plan year by year: taxes, Required Minimum Distributions, Social Security, Roth conversions and withdrawals. Then it stress-tests that plan against 5,000 simulated markets and every historical period since 1928. An AI coach sits on top of all of it, so you can ask plain-English questions about your own numbers.',
            'It\'s built for people planning their own retirement, not for selling financial products. There\'s also a plan for financial advisors who want to bring clients onto the platform under their own branding.',
        ],
        'highlights': [
            ('5,000', 'Monte Carlo scenarios per simulation'),
            ('1928–2024', 'historical market data for backtesting'),
            ('81', 'Social Security claiming-age combinations compared'),
            ('50 + DC', 'states modeled for income tax'),
        ],
        'feature_groups': [
            {
                'title': 'Planning',
                'items': [
                    'AI retirement coach that answers questions about your plan in plain English',
                    'Readiness score built from five parts: Monte Carlo success, portfolio sustainability, income adequacy, savings rate and tax diversification',
                    'Projected portfolio value at your target retirement age, with year-by-year growth',
                    'Up to 20 what-if scenarios compared side by side',
                    'Guided setup in about 15 minutes',
                ],
            },
            {
                'title': 'Income & withdrawals',
                'items': [
                    'Social Security, pensions, rental income and dividends, adjusted for inflation',
                    'Monte Carlo odds of success with P10 / P50 / P90 outcomes',
                    'Historical backtest heatmap across every decade since 1928',
                    'Five withdrawal strategies: the 4% rule, spend-more-early, market-based, Guyton-Klinger guardrails and Vanguard dynamic spending, all on one chart',
                    'Early-retirement bridge to age 59½: penalty-free accounts, Roth conversion ladders and Rule 72(t)',
                ],
            },
            {
                'title': 'Taxes',
                'items': [
                    'Federal tax from the actual IRS brackets for your filing status',
                    'State income tax for all 50 states plus DC',
                    'Social Security taxation based on provisional income, and FICA per spouse',
                    'RMD projections by account type (age 73 or 75)',
                    'Roth conversion planner showing tax cost per year and lifetime savings',
                    'Social Security optimizer across all 81 claiming-age combinations, including spousal and survivor benefits',
                ],
            },
            {
                'title': 'Tools & integrations',
                'items': [
                    'Annuity modeling: SPIAs, deferred income annuities and QLACs',
                    'Budget phases for different stages of life, plus one-time expenses and debt',
                    'Contribution tracking for every account',
                    'Net worth, cash flow and income reports, plus a 9-page PDF export',
                    'Monarch Money import to update every balance from one CSV',
                    'AI connector: link Claude or ChatGPT to your plan with a read-only, revocable OAuth sign-in',
                ],
            },
        ],
        'plans': [
            {
                'name': 'Free',
                'price': '$0',
                'period': 'forever',
                'features': [
                    'Interactive retirement dashboard',
                    'Portfolio & account tracking',
                    'Income stream planning',
                    'Expense budgeting',
                    '5 AI coach conversations',
                    '1 Monte Carlo simulation',
                    'No credit card required',
                ],
            },
            {
                'name': 'Unlimited',
                'price': '$9.99',
                'period': 'per month',
                'highlight': True,
                'features': [
                    'Everything in Free',
                    'More AI coach conversations',
                    'Unlimited Monte Carlo simulations',
                    'Detailed financial reports',
                    'Up to 20 what-if scenarios',
                    'Connect Claude or ChatGPT to your plan',
                    'Priority support',
                    'Cancel anytime',
                ],
            },
            {
                'name': 'Financial Advisor',
                'price': 'Custom',
                'period': 'based on practice size',
                'features': [
                    'Bring your clients onto the platform',
                    'Your firm\'s branding',
                ],
            },
        ],
        'how_it_works': [
            'Enter your age, retirement goal and spending target',
            'Add your accounts, contributions and income sources, or import balances from Monarch Money',
            'See your readiness score, cash flow and year-by-year projection',
            'Run Monte Carlo and historical simulations to see how the plan holds up',
            'Try what-if scenarios and ask the AI coach what would change the outcome',
        ],
        'faqs': [
            {
                'question': 'Who is RetirePlanAI for?',
                'answer': 'People planning their own retirement, whether you\'re just starting to think about it or a few years out. There\'s also a separate plan for financial advisors.',
            },
            {
                'question': 'Is it free?',
                'answer': 'Yes. The Free plan includes the dashboard, account tracking, income and expense planning, 5 AI coach conversations and 1 Monte Carlo simulation, with no credit card. The Unlimited plan is $9.99/month.',
            },
            {
                'question': 'Can I use it with Claude or ChatGPT?',
                'answer': 'Yes. The Unlimited plan includes an AI connector that lets Claude or ChatGPT read your plan through a secure OAuth sign-in. Access is read-only and you can revoke it at any time.',
            },
            {
                'question': 'What happens to my data?',
                'answer': 'It\'s protected with industry-standard security, and payments go through Stripe. Your data is never sold or shared with third parties.',
            },
            {
                'question': 'Is this financial advice?',
                'answer': 'No. RetirePlanAI is for informational and planning purposes only.',
            },
        ],
    },
    {
        'slug': 'ttp-appointments',
        'name': 'TTP Appointments',
        'url': 'https://ttpappointments.com',
        'logo': 'base/images/ttp-logo.png',
        'status': 'Live',
        'year': '2023',
        'featured': True,
        'summary': 'Email and text alerts the moment a Global Entry interview slot opens up.',
        'tagline': 'Get alerted when Global Entry interview appointments open up.',
        'stack': ['Django', 'Python', 'Stripe', 'Twilio'],
        'description': [
            'I built TTP Appointments in high school, in February 2023. Getting a Global Entry interview meant refreshing the government scheduler over and over, so I wrote something to do it for me.',
            'It checks the Trusted Traveler Program scheduler around the clock and sends an email and text as soon as a slot opens at the enrollment centers you pick. You still book the appointment yourself on the official site.',
        ],
        'features': [
            'Free alert with no credit card and no charges',
            'One month of alerts, no recurring charges',
            'Email and text message alerts',
            'Auto-reactivating alerts',
            'Custom date range',
            '100% satisfaction guaranteed or your money back',
        ],
        'plans': [
            {
                'name': 'Free',
                'price': '$0',
                'period': 'one alert',
                'features': [
                    'Choose up to 1 enrollment center',
                    'All enrollment centers supported',
                    'Up to 3 email alerts',
                    'No credit card required',
                    'Upgrade anytime',
                ],
            },
            {
                'name': 'Paid',
                'price': '$24.99',
                'period': 'one-time',
                'highlight': True,
                'features': [
                    'Choose up to 5 enrollment centers',
                    'All enrollment centers supported',
                    'Unlimited email and text alerts',
                    'Auto-reactivating alerts',
                    'Custom date range',
                    'No recurring payments',
                    '100% satisfaction guaranteed or your money back',
                ],
            },
        ],
        'how_it_works': [
            'Create an alert for the enrollment centers you want',
            'TTP Appointments checks for openings 24/7',
            'You get an email and text when an interview slot opens',
            'Book the appointment directly on the Trusted Traveler Program website',
        ],
        'faqs': [
            {
                'question': 'How does TTP Appointments work?',
                'answer': 'It checks for openings 24/7 and sends you an email and text when an interview appointment becomes available at the centers you chose. You then book the appointment directly on the Trusted Traveler Program website. The free plan includes up to 3 email alerts.',
            },
            {
                'question': 'Am I guaranteed to get an appointment at the enrollment center I choose?',
                'answer': 'No. It checks every 5 minutes and notifies you when there\'s an opening, but someone else may book the slot before you do.',
            },
            {
                'question': 'Will the alert book my appointment?',
                'answer': 'No. After you get an alert, it\'s up to you to make the appointment.',
            },
            {
                'question': 'Are you affiliated with the US Government or the Trusted Traveler Program?',
                'answer': 'No. TTP Appointments is an independent service and is not affiliated with the US Government or the Trusted Traveler Program.',
            },
        ],
        'featured_in': ['The Points Guy', 'NerdWallet', 'Patch News', 'Livermore Independent'],
    },
    {
        'slug': 'willo-decisions',
        'name': 'Willo Decisions',
        'url': 'https://willodecisions.com',
        'logo': 'base/images/willo-logo.png',
        'status': 'Live',
        'year': '2024',
        'featured': True,
        'summary': 'Group decision-making using the Choosing By Advantages method.',
        'tagline': 'Sharpen thinking. Simplify deciding. Rest easy.',
        'stack': ['Django', 'Python', 'REST APIs'],
        'description': [
            'I built Willo in May 2024, the summer between high school and community college. It\'s a tool for making decisions as a group using Choosing By Advantages (CBA).',
            'Instead of weighted scores, CBA has you compare the actual advantages of each option. In Willo you set up a project with your factors and options, invite collaborators, and work through the comparison together with charts that show where things landed.',
        ],
        'features': [
            'Collaborative decision-making projects',
            'Choosing By Advantages (CBA) method',
            'Invite unlimited collaborators by email',
            'Charts and graphs of the decision',
            'Custom factors and options',
            'Revisit and adjust decisions at any time',
        ],
        'how_it_works': [
            'Create a project with your decision factors and options',
            'Invite collaborators by email',
            'Identify and compare the advantages of each option',
            'Review the charts to see how the options stack up',
            'Adjust rankings as your thinking changes',
        ],
        'faqs': [
            {
                'question': 'What is the Choosing By Advantages (CBA) method?',
                'answer': 'CBA focuses on identifying and comparing the advantages of each option rather than relying only on numerical scores, so decisions are based on real benefits and trade-offs.',
            },
            {
                'question': 'How do I invite collaborators?',
                'answer': 'Add their email addresses in the project settings and share the project link. Once they join, they can contribute to the decision.',
            },
            {
                'question': 'How is Willo different from a decision matrix?',
                'answer': 'Traditional decision matrices rely on numerical scores and weights. Willo uses CBA, which compares the advantages of each option directly.',
            },
            {
                'question': 'Can I change my decisions later?',
                'answer': 'Yes. You can go back to earlier steps, change your rankings and update the project whenever you need to.',
            },
            {
                'question': 'Is there a limit on collaborators?',
                'answer': 'No. You can invite as many people as you need.',
            },
        ],
    },
    {
        'slug': 'magic-dining-alerts',
        'name': 'Magic Dining Alerts',
        'url': '',
        'logo': 'base/images/magic-dining-logo.png',
        'logo_on_dark': True,  # white logo, needs a dark backdrop
        'status': 'Offline',
        'summary': 'Alerts for hard-to-get Walt Disney World and Disneyland dining reservations.',
        'tagline': 'Notifications for Walt Disney restaurant reservations.',
        'stack': ['Django', 'Python', 'REST APIs'],
        'description': [
            'Magic Dining Alerts watched Disney restaurant availability and sent an alert when a reservation opened up at the restaurants you picked, so you could book it through Disney before it was gone.',
        ],
        'features': [
            'Email and SMS notifications',
            'Real-time reservation alerts',
            'Monitor multiple restaurants at once',
            'Quick sign-up',
        ],
        'how_it_works': [
            'Sign up for alerts on specific Disney restaurants',
            'The service monitors reservation availability',
            'You get a notification when a reservation opens',
            'Book directly through Disney',
        ],
        'faqs': [
            {
                'question': 'Which Disney restaurants were supported?',
                'answer': 'All Walt Disney World and Disneyland restaurants that accept reservations through the Disney dining system.',
            },
        ],
    },
    {
        'slug': 'ai-bible-guide',
        'name': 'AI Bible Guide',
        'url': '',
        'logo': None,
        'status': 'In development',
        'summary': 'A native iOS app for reading scripture with AI-powered explanations and context.',
        'tagline': 'Read scripture with explanations and context alongside.',
        'stack': ['Swift', 'Firebase', 'OpenAI'],
        'description': [
            'AI Bible Guide is a native iOS app I\'m building for reading and studying the Bible. Tap a verse to get an explanation, historical context and how it connects to the rest of scripture, or ask your own questions as you read.',
        ],
        'features': [
            'Verse explanations and historical context',
            'Ask questions while you read',
            'Personalized study suggestions',
            'Search across scripture',
            'Save favorite verses and notes',
            'Sync across iPhone and iPad with Firebase',
        ],
        'how_it_works': [
            'Browse books, chapters and verses',
            'Tap any verse for an explanation',
            'Ask follow-up questions',
            'Save verses and notes and pick up on any device',
        ],
        'faqs': [
            {
                'question': 'What Bible translations are available?',
                'answer': 'The app will include several popular translations. More details once it launches.',
            },
            {
                'question': 'Is this a native iOS app?',
                'answer': 'Yes. It\'s written in Swift for iPhone and iPad.',
            },
        ],
    },
]

PROJECTS_BY_SLUG = {p['slug']: p for p in PROJECTS}


def home(request):
    """Home page view"""
    context = {
        'title': 'Home',
        'projects': PROJECTS,
    }
    return render(request, 'base/home.html', context)

def projects(request):
    """Projects listing page view"""
    context = {
        'title': 'Projects',
        'page_title': 'Projects',
        'projects': PROJECTS,
    }
    return render(request, 'base/projects.html', context)

def project_detail(request, project_slug):
    """Individual project detail page view"""
    project = PROJECTS_BY_SLUG.get(project_slug)
    if not project:
        raise Http404(f"Project '{project_slug}' not found.")

    context = {
        'title': project['name'],
        'page_title': project['name'],
        'project': project,
    }
    return render(request, 'base/project_detail.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About',
        'page_title': 'About',
        'projects': PROJECTS,
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
