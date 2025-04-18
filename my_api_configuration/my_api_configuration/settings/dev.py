from .base import *
import environ


env = environ.Env()
environ.Env.read_env(str(HOME_DIR / ".env"))
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ['18.159.50.123', 'localhost']
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
