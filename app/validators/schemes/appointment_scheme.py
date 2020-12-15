from pydantic import BaseModel, validator, ValidationError
from datetime import datetime
from typing import Optional

class AppointmentScheme(BaseModel):
    doctor_id: str
    patient_id: str
    startDateTime: datetime
    finishDateTime: datetime
    note: Optional[str]
