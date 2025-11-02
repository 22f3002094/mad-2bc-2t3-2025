
class LocalConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.sqlite3"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "thisissalt"
