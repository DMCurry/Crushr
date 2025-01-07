from sqlalchemy.orm import Session


class BaseService:
    def __init__(self, db: Session, auth: object = None):
        """
        Base service class to share dependencies.

        Args:
            db (Session): The database session.
            auth (object): Authentication-related utilities (e.g., token manager).
        """
        self.db = db
        self.auth = auth