import uvicorn
import logging
import sys

# Send all DEBUG+ logs to stdout in a simple format
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

logging.getLogger("uvicorn").setLevel(logging.DEBUG)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, exercises, login, logout, check_auth, training_plan, schedule, performance_test, analytics
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import MetaData
from app.core.db import engine
from models import Base


app = FastAPI()

# Define the origins that should be allowed
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://crushr.org",
    "http://www.crushr.org",
    "http://143.198.235.252",
]

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(users.router)
app.include_router(exercises.router)
app.include_router(login.router)
app.include_router(logout.router)
app.include_router(check_auth.router)
app.include_router(training_plan.router)
app.include_router(schedule.router)
app.include_router(performance_test.router)
app.include_router(analytics.router)

# Create tables from models (Commented out bc it conflicts with alembic managing things now)
#Base.metadata.create_all(engine)

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

@app.middleware("http")
async def log_every_request(request, call_next):
    print("🔥 got request:", request.method, request.url.path)
    return await call_next(request)

