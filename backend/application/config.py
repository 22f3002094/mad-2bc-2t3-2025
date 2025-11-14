
class LocalConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.sqlite3"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "thisissalt"
    SECRET_KEY = "supersecretkey"
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_DEFAULT_TIMEOUT = 30 
    CELERY_BROKER_URL = 'redis://localhost:6379'