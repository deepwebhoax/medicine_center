<<<<<<< HEAD
from app.data.database.database import MongoBase
from typing import Sequence, Tuple


class MessagesCollection(MongoBase):
    collection_name: str = 'message'
    db_fields: Sequence[Tuple[str]] = ('_id', 'doctor_id', 'patient_id', 'sender', 'text', 'dateCreated')

    
||||||| merged common ancestors
=======
from app.database.database import MongoBase
from typing import Sequence, Tuple


class MessagesCollection(MongoBase):
    collection_name: str = 'message'
    db_fields: Sequence[Tuple[str]] = ('_id', 'doctor_id', 'patient_id', 'sender', 'text', 'dateCreated')

    
>>>>>>> 7502b1f49ac5e4efb7074a3866b964592d53af6b
