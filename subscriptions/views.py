from django.shortcuts import render, redirect
from django.conf import settings
from .models import Plan
from .services import create_stripe_checkout_session

def pricing(request):
    plans = Plan.objects.all()
    return render(request, 'landing/home.html#pricing', {'plans': plans}) # Actually handled in landing

def checkout(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    # Assuming Stripe for now as primary
    if plan.stripe_price_id:
        url = create_stripe_checkout_session(request.user, plan.stripe_price_id)
        if url:
            return redirect(url)
    return redirect('dashboard_billing')
