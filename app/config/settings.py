import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:password@localhost:3306/customerdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}
    
    # Additional configuration settings
    THREADS_PER_PAGE = 8
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'dev-csrf-secret-key'
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)