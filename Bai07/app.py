import os

app_env = os.environ.get("APP_ENV", "unknown")
print(f"Current environment: {app_env}")
