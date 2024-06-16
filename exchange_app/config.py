class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///products.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    EX_RATE_API_KEY = '73e7ed75084bd6a819952125'
    EX_RATE_BASE_URL = 'https://v6.exchangerate-api.com/v6'
