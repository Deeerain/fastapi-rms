from os import environ

DB_NAME = environ.get('DB_NAME', 'rms')
DB_USER = environ.get('DB_USER', 'rms-user')
DB_PASSWORD = environ.get('DB_PASSWORD', 'rms')
DB_HOST = environ.get('DB_HOST', 'localhost')
DB_PORT = environ.get('DB_PORT', 5432)
DB_CONNECTION_STRING = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'