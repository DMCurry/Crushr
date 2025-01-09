import json
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.weekly_schedule import WeeklySchedule
from models.exercise import Exercise
from models.performance_test import PerformanceTest
from models.training_plan import TrainingPlan
from models.user import User

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqldb://root:@localhost:3306/mydb")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, future=True)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_and_insert_data(jf, model_name):
    try:
        with open(jf, 'r') as filename:
            data = json.load(filename)
            with SessionLocal() as session:
                for record in data:
                    print(jf)
                    instance = model_class(**record)
                    #print(instance)
                    session.add(instance)  # Unpack JSON data
                session.commit()
        print(f"Inserted data from {jf} into {model_name.__name__}")
    except Exception as e:
        print("E", e)
        print(f"Error inserting data from {jf}: {e}")

# Main execution block
if __name__ == "__main__":
    path = "seed_data/"
    # List of JSON files and corresponding models
    json_files_and_models = [
        (path + "users.json", User),
        (path + "training_plan.json", TrainingPlan),
        (path + "exercise.json", Exercise),
        (path + "performance_test.json", PerformanceTest),
        (path + "weekly_schedule.json", WeeklySchedule)
    ]

    # Loop over the JSON files and insert data
    for json_file, model_class in json_files_and_models:
        load_and_insert_data(json_file, model_class)