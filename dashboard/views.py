from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from listings.forms import ListingForm
from listings.services import generate_listing_description
from listings.models import Listing

@login_required
def overview(request):
    recent_listings = Listing.objects.filter(user=request.user).order_by('-created_at')[:5]
    count = Listing.objects.filter(user=request.user).count()
    return render(request, 'dashboard/overview.html', {'recent_listings': recent_listings, 'count': count})

@login_required
def generate_description(request):
    generated_description = None
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            # Call DeepSeek API
            description = generate_listing_description(form.cleaned_data)
            listing.generated_description = description
            listing.save()
            generated_description = description
    else:
        form = ListingForm()
    
    return render(request, 'dashboard/generate.html', {'form': form, 'generated_description': generated_description})

@login_required
def my_listings(request):
    listings = Listing.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard/listings.html', {'listings': listings})

@login_required
def billing(request):
    return render(request, 'dashboard/billing.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')
