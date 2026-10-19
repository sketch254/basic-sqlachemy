# # 1. Base Configuration with Fallback URI
# class BaseConfig:
#     SQLALCHEMY_DATABASE_URI = os.getenv(
#         "<DB_ENV_NAME>", "<driver>:///\<default location\>"
#     )
# # 2. Environment Overrides (Dev, Test, Prod)
# class <Env>Config(BaseConfig):
#     <flags such as DEBUG or TESTING>
#     SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:" # If needed
# # 3. App Factory Configuration Dictionary
# CONFIGS = {
#     "<env name>": <Env>Config
# }

# import os
# from dotenv import load_dotenv

# load_dotenv()

class Config:
    # Secret key for sessions and CSRF protection
    SECRET_KEY = "dev-secret-change-in-production"

    # Database URI: SQLite for dev, override with DATABASE_URL env var for prod
    SQLALCHEMY_DATABASE_URI = "sqlite:///user_profile.db"

    # Disable legacy event system to reduce overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Echo SQL to stdout in debug mode (set False in production)
    SQLALCHEMY_ECHO = "1"

class TestConfig(Config):
    # In-memory database for tests; wiped after each run
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
    WTF_CSRF_ENABLED = False


CONFIGS = {
    "default": Config,
    "testing" : TestConfig
}
