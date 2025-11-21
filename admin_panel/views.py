from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from subscriptions.models import Subscription, Plan, Payment
from listings.models import Listing

User = get_user_model()

def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = User.objects.count()
    active_subscriptions = Subscription.objects.filter(active=True).count()
    total_listings = Listing.objects.count()
    recent_users = User.objects.order_by('-date_joined')[:5]
    
    context = {
        'total_users': total_users,
        'active_subscriptions': active_subscriptions,
        'total_listings': total_listings,
        'recent_users': recent_users,
    }
    return render(request, 'admin_panel/dashboard.html', context)

@user_passes_test(is_admin)
def users_list(request):
    users = User.objects.all()
    return render(request, 'admin_panel/users.html', {'users': users})

@user_passes_test(is_admin)
def plans_list(request):
    plans = Plan.objects.all()
    return render(request, 'admin_panel/plans.html', {'plans': plans})

@user_passes_test(is_admin)
def payments_list(request):
    payments = Payment.objects.all().order_by('-date')
    return render(request, 'admin_panel/payments.html', {'payments': payments})
