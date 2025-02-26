from passlib.context import CryptContext
import enum

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


class ItemType(enum.Enum):
    TEST = 1
    EXERCISE = 2

class Weekday(enum.Enum):
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"

def hash_password(password: str) -> str:
    return PWD_CONTEXT.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)