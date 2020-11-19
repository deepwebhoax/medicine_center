from .database import MongoBase
from typing import Sequence, Tuple


class ScheduleCollection(MongoBase):
    collection_name: str = 'schedule'
    db_fields: Sequence[Tuple[str]] = ('_id', 'doctor', 'weekDay', 'startDateTime', 'finishDateTime', 'hospital', 'room')
