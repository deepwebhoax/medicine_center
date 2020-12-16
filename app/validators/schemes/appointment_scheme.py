from pydantic import BaseModel, validator, ValidationError, root_validator
from datetime import datetime
from typing import Optional
from app.api.repository import Repository

class AppointmentScheme(BaseModel):
    doctor_id: str
    patient_id: str
    startDateTime: datetime = None
    finishDateTime: datetime = None
    note: Optional[str]
    
    # is start time out of doctor's schedule
    # @validator('startDateTime', pre=True)
    # def within_working_hours(cls, v, values):
    #     schedule = Repository.get_schedule(values['doctor_id'])
    #     workingHours = [(s['startTime'], s['finishTime'])
    #                     for s in schedule if s['weekDay']==v.strftime('%A')] # get working hours on the appointment day
    #     for start, finish in workingHours:
    #         if start < v < finish:
    #             return v
    #     raise ValueError(f'Doctor is working today at {workingHours}')
        

    # time is occupied by other patients
    # @validator('finishDateTime')
    @root_validator()
    def is_unoccupied(cls, values):
        doctors_appointments = Repository.get_appointments_by_doctor(values['doctor_id'])
        for a in doctors_appointments:
            print('a=', a, 'values', values)
            if a['startDateTime'] <= values['startDateTime'] <= a['finishDateTime']  or a['startDateTime'] <= values['finishDateTime'] <= a['finishDateTime']:
                print('ERRRRRRRORRRRRRRRRRRRRRRRRRRRRRRR, occupied')
                raise ValueError('Time overlaps with existing appointment')
        return values    

    # @validator('startDateTime', pre=True)
    # def is_soon(cls, v):
    #     maxForward = 2*7*24*60*60 # (2 weeks) maximum time in sec between appointment time and now  
    #     if v.timestamp() - datetime.datetime.today().timestamp() > maxForward:
    #         raise ValueError('Making appointments ')
    #     return v

    # no longer then 2 hours
    # @validator('startDateTime', 'finishDateTime')
    @root_validator()
    def is_short(cls, values):
        if values['finishDateTime'].timestamp() - values['startDateTime'].timestamp() > 2*60*60:
            raise ValueError('Appointments longer then 2 hours are not allowed')

        return values