import json
import shutil
import uuid
import os

from fastapi import APIRouter, File, UploadFile

# add correct db classes. create if don't exist
# from app.validators.schemes.user_schemes import DiseaseHistoryScheme
from app.validators.schemes.user_schemes import ScheduleScheme
from app.database.doctor import DoctorCollection
from app.database.patient import PatientCollection
from app.database.hospital import HospitalCollection
from app.database.schedule import ScheduleCollection


router = APIRouter()

@router.get('/schedule/{doctor_id}')
async def get_schedule(doctor_id: int, weekDay: str):
    """
    Get doctor's schedule
    TODO: make it not so kalechnum
    :param doctor_id:
    :return: schedule_data
    """
    schedule_data = ScheduleCollection.get_all_objects({'doctor': str(doctor_id), 'weekDay': weekDay})

    return schedule_data



@router.post('/schedule/add/{doctor_id}')
async def get_patient_profile(doctor_id: str, schedule: ScheduleScheme):
    """
    Add schedule for doctor in hospital x
    TODO: load data from database
    :param doctor_id: 
    :param schedule_id: 
    :return: status
    """
    patient_data = ScheduleCollection.get_one_obj({'user_id': patient_id})


    return patient_data

@router.put('/schedule/update/{doctor_id}')
async def get_patient_profile(doctor_id: str, new_schedule: Schedule):
    """
    Add schedule for doctor in hospital x
    TODO: load data from database
    :param patient_id: 
    :param history_id: 
    :return: 
    """
    patient_data = ScheduleCollection.update_obj_by_id( doctor_id, dict(new_schedule))


    return patient_data
