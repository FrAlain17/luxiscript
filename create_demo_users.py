import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luxiscript.settings')
django.setup()

from django.contrib.auth import get_user_model
from subscriptions.models import Plan, Subscription

User = get_user_model()

def create_demo_accounts():
    # Create Admin User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        print("Superuser 'admin' created.")
    else:
        print("Superuser 'admin' already exists.")

    # Create Standard User
    if not User.objects.filter(username='demo_user').exists():
        user = User.objects.create_user('demo_user', 'demo@example.com', 'demopassword')
        print("User 'demo_user' created.")
        
        # Create Basic Plan if it doesn't exist
        plan, created = Plan.objects.get_or_create(
            slug='basic',
            defaults={
                'name': 'Basic Plan',
                'price': 9.99,
                'description_quota': 10,
                'stripe_price_id': 'price_dummy_basic',
                'paypal_plan_id': 'plan_dummy_basic'
            }
        )
        if created:
            print("Plan 'Basic Plan' created.")
        
        # Create Subscription for the user
        Subscription.objects.create(
            user=user,
            plan=plan,
            active=True,
            current_period_end=timezone.now() + timezone.timedelta(days=30)
        )
        print("Subscription created for 'demo_user'.")
        
    else:
        print("User 'demo_user' already exists.")

if __name__ == '__main__':
    create_demo_accounts()
