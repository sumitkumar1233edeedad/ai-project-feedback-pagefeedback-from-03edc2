import os

class Config:
    APP_NAME = os.getenv('APP_NAME', 'AI Project')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
