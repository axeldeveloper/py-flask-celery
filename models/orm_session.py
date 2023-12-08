import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from setting.config import DevelopmentConfig
#DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_URL = DevelopmentConfig.DATABASE_URL
engine = create_engine(DATABASE_URL, pool_recycle=3600, pool_size=10)
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()