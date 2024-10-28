from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.config import settings

# Define the base for the ORM models
Base = declarative_base()

# Create the database engine
engine = create_engine(settings.DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
