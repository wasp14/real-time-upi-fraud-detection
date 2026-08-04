from storage_service.database import engine
from storage_service.models import Base

def init_db():
    Base.metadata.create_all(engine)