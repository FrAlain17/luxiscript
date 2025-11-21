from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.users_list, name='admin_users'),
    path('plans/', views.plans_list, name='admin_plans'),
    path('payments/', views.payments_list, name='admin_payments'),
]
