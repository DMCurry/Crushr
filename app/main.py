import uvicorn
from fastapi import FastAPI
from app.routers import users, exercises
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import MetaData
from models import Base


app = FastAPI()

app.include_router(users.router)
app.include_router(exercises.router)

# Database URL
DATABASE_URL = "mysql+mysqldb://root:@localhost:3306/mydb"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

#Create tables from models
Base.metadata.create_all(engine)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Connection test function
def test_database_connection():
    try:
        # Attempt to connect to the database
        with engine.connect() as connection:
            print("Connection successful!")

            # Test if the database exists by querying a simple SELECT statement
            result = connection.execute(text("SELECT DATABASE()"))
            db_name = result.scalar()  # This fetches the first column of the first row
            print(f"Connected to database: {db_name}")

            # Try a basic SQL query to ensure the connection works
            result = connection.execute(text("SELECT 1"))
            print(f"Query result: {result.scalar()}")  # Use scalar to get the first result value

    except OperationalError as e:
        print(f"Error: Unable to connect to the MySQL server. Details: {e}")
    except ProgrammingError as e:
        print(f"Error: There was an issue with the SQL query. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# FastAPI startup event to test the database connection
@app.on_event("startup")
async def startup_event():
    test_database_connection()
    print("FastAPI app started and connected to the MySQL database.")

@app.get("/")
async def root():
    return {"message": "testing app ok"}