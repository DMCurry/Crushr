import json
from app.main import SessionLocal
from models.weekly_schedule import WeeklySchedule
from models.exercise import Exercise
from models.performance_test import PerformanceTest
from models.training_plan import TrainingPlan
from models.user import User


def load_and_insert_data(filename, model_name):
    try:
        with open(json_file, 'r') as filename:
            data = json.load(filename)
            with SessionLocal() as session:
                for record in data:
                    instance = model_class(**record)
                    session.add(instance)  # Unpack JSON data
                session.commit()
        print(f"Inserted data from {filename} into {model_name.__name__}")
    except Exception as e:
        print(f"Error inserting data from {filename}: {e}")

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