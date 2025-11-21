from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='dashboard_overview'),
    path('generate/', views.generate_description, name='dashboard_generate'),
    path('listings/', views.my_listings, name='dashboard_listings'),
    path('billing/', views.billing, name='dashboard_billing'),
    path('profile/', views.profile, name='dashboard_profile'),
]
