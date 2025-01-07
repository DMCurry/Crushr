from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Database URL
DATABASE_URL = "mysql+mysqldb://root:@localhost:3306/mydb"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, future=True)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)