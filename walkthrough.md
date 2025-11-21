# LuxiScript Walkthrough

## Overview
LuxiScript is a multi-tenant SaaS application for generating real estate listing descriptions using AI.

## Features Implemented
- **Landing Page**: Modern, responsive landing page with features, pricing, and FAQ.
- **Authentication**: Custom user model, signup, login, logout.
- **Client Dashboard**:
    - Overview with stats.
    - Generate Description using DeepSeek API.
    - My Listings history.
    - Billing & Profile placeholders.
- **Admin Dashboard**:
    - Custom admin panel with KPIs.
    - User management.
    - Plan management.
    - Payment history.
- **Subscriptions**:
    - Stripe and PayPal integration services.
    - Subscription models.
- **Deployment**:
    - Dockerfile and docker-compose.yml ready for Coolify.

## How to Run Locally

1.  **Environment Setup**:
    Ensure your `.env` file has the correct API keys:
    ```bash
    DEEPSEEK_API_KEY=your_key
    STRIPE_SECRET_KEY=your_key
    # ... other keys
    ```

2.  **Run with Docker**:
    ```bash
    docker-compose up --build
    ```

3.  **Run Manually**:
    ```bash
    source venv/bin/activate
    python manage.py migrate
    python manage.py runserver
    ```

4.  **Access the App**:
    - Landing Page: `http://localhost:8000/`
    - Dashboard: `http://localhost:8000/dashboard/`
    - Admin Panel: `http://localhost:8000/admin-panel/` (Login with `admin` / `adminpassword`)

## Verification
- **Migrations**: All migrations applied successfully.
- **Superuser**: Created default admin user.
- **Tailwind**: CSS compiled to `static/css/output.css`.

## Next Steps
- Connect real Stripe/PayPal webhooks.
- Deploy to Coolify using the provided Docker configuration.
