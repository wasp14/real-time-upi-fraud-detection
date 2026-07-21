from storage_service.database import engine
from storage_service.models import Base


Base.metadata.create_all(engine)