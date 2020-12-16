from pydantic import BaseModel, validator, ValidationError
from datetime import datetime
from typing import Optional
from app.api.repository import Repository

class AppointmentScheme(BaseModel):
    doctor_id: str
    patient_id: str
    startDateTime: datetime
    finishDateTime: datetime
    note: Optional[str]
    
    # is start time out of doctor's schedule
    @validator('startDateTime')
    def within_working_hours(cls, v, values):
        schedule = get_schedule(values['doctor_id'])
        workingHours = [(s[startTime], s[finishTime]) if s[weekDay]==v.strftime('%A') 
                        for s in schedule] # get working hours on the appointment day
        for start, finish in workingHours:
            if start<v<finish:
                return v
        raise ValueError(f'Doctor is working today at {wokringHours}')
        

    # time is occupied by other patients
    @validator('startDateTime')
    def is_unoccupied(cls):
        schedule = get_schedule(values['doctor_id'])

        return False    

    @validator('startDateTime')
    def is_soon(cls, v):
        maxForward = 2*7*24*60*60 # (2 weeks) maximum time in sec between appointment time and now  
        if v.timestamp() - datatime.datetime.today().timestamp() > maxForward:
            raise ValueError('Making appointments ')
        return v

    # no longer then 2 hours
    @validator('startDateTime', 'finishDateTime')
    def is_short(cls, v, values):
        if values['finishDateTime'].timestamp() - values['startDateTime'].timestamp() > 2*60*60:
            raise ValueError('Appointments longer then 2 hours are not allowed')

        return v