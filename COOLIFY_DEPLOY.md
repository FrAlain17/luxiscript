# Deploying LuxiScript to Coolify

This guide explains how to deploy your Django application to Coolify using the provided configuration.

## Prerequisites

- A running instance of Coolify (self-hosted or cloud).
- This project pushed to a Git repository (GitHub, GitLab, etc.).

## Configuration Files

We have prepared the following files for production deployment:

1.  **`Dockerfile`**: Builds the Python environment, installs dependencies, and sets up the entrypoint.
2.  **`entrypoint.sh`**: Runs automatically on container start. It applies database migrations and collects static files.
3.  **`docker-compose.prod.yml`**: Defines the `web` (Django) and `db` (PostgreSQL) services.
4.  **`requirements.txt`**: Includes `gunicorn`, `psycopg2-binary`, `dj-database-url`, and `whitenoise` for production.
5.  **`settings.py`**: Configured to read database credentials from `DATABASE_URL` and serve static files via Whitenoise.

## Deployment Steps in Coolify

1.  **Create a New Resource**:
    - Go to your Coolify dashboard.
    - Click "+ New" -> "Project" -> "Production" (or your environment).
    - Select "Git Repository" (public or private).

2.  **Select Repository**:
    - Choose your repository containing the LuxiScript code.
    - Branch: `main` (or `master`).

3.  **Build Pack**:
    - Coolify might auto-detect "Docker Compose" or "Dockerfile".
    - **Recommended**: Select **Docker Compose**.
    - If asked for the compose file path, enter: `docker-compose.prod.yml`.

4.  **Environment Variables**:
    - Before deploying, go to the "Environment Variables" tab for your service.
    - Add the following secrets (copy from your local `.env` but update for production):
        - `SECRET_KEY`: (Generate a strong random string)
        - `DEBUG`: `False`
        - `ALLOWED_HOSTS`: `your-coolify-domain.com` (or `*` for testing)
        - `DEEPSEEK_API_KEY`: `...`
        - `STRIPE_PUBLIC_KEY`: `...`
        - `STRIPE_SECRET_KEY`: `...`
        - `PAYPAL_CLIENT_ID`: `...`
        - `PAYPAL_CLIENT_SECRET`: `...`
        - `PAYPAL_MODE`: `live`
    - **Note**: You do *not* need to set `DATABASE_URL` manually if Coolify manages the database within the stack, but if you are using the `docker-compose.prod.yml` provided, Coolify will spin up a Postgres container named `db`. The `web` service is configured to connect to `postgres://luxiscript:luxiscript@db:5432/luxiscript`.
    - **Important**: For better security in production, you should change the Postgres password in `docker-compose.prod.yml` and update the `DATABASE_URL` env var accordingly, OR use Coolify's built-in PostgreSQL database service and link it.

5.  **Deploy**:
    - Click "Deploy".
    - Watch the logs.
    - The `entrypoint.sh` will run migrations and collect static files automatically.

6.  **Verify**:
    - Open the URL provided by Coolify.
    - Log in with the superuser (you may need to create one via terminal if not using the local sqlite db).
    - To create a superuser in production:
        - Go to Coolify -> Your Service -> Terminal/Console.
        - Run: `python manage.py createsuperuser`

## Troubleshooting

- **Static Files 404**: Ensure `Whitenoise` is configured (it is) and `collectstatic` ran (check logs).
- **Database Error**: Check `DATABASE_URL` and ensure the `db` service is healthy.

### Common Deployment Errors

**Error: `fatal: could not read Username for 'https://github.com': No such device or address`**

This means Coolify cannot authenticate with your GitHub repository. This happens if:
1.  The repository is **Private** and you haven't connected a GitHub App or Token.
2.  Coolify is trying to access via HTTPS without credentials.

**Solution:**
1.  **Best Method**: Go to Coolify "Sources" -> "Git Sources" -> "GitHub.com" and connect a GitHub App. Then, when creating the resource, select the repository from the list instead of pasting the URL.
2.  **Alternative**: Use a Personal Access Token (PAT) in the URL: `https://<token>@github.com/FrAlain17/luxiscript.git`.
3.  **Public Repo**: If the repo is public, ensure you selected "Public Repository" when creating the resource in Coolify.

**Error: `DisallowedHost at /` or `Invalid HTTP_HOST header`**

This means Django is blocking the request because the domain name is not in the `ALLOWED_HOSTS` list.

**Solution:**
1.  Go to Coolify -> Your Service -> Environment Variables.
2.  Edit `ALLOWED_HOSTS`.
3.  **Ensure it is NOT empty.**
4.  Add your domain: `listingcraft.online` (or whatever domain you are using).
    - Example: `listingcraft.online,www.listingcraft.online,localhost`
5.  **Also set `DEBUG` to `False`.**
6.  Redeploy.

**Note**: If you see `ALLOWED_HOSTS []` in the error debug page, it means you have defined the variable `ALLOWED_HOSTS` but left it empty. You must provide a value.
