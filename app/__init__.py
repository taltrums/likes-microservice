from flask import Flask
from flask_caching import Cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config.Config')

# Initialize cache
cache = Cache(app)

# Database configuration
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models after initializing app and database
from app import routes

# Create the database tables within the application context
with app.app_context():
    db.create_all()
