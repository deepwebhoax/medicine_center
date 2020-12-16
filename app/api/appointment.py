from fastapi import APIRouter

from app.api.repository import Repository

from app.validators.schemes.appointment_scheme import AppointmentScheme
from app.database.appointment import AppointmentsCollection
from app.database.schedule import ScheduleCollection

router = APIRouter()


@router.post('/appointment/add')
async def add_appointment(appointment:dict):
    """
    Adds an appointment of patient with a doctor
    :param appointment: dictionary containing appointment details
    :return: status
    """
    print('appointment')
    status = Repository.add_appointment(appointment)

    return status

@router.delete('/appointment/delete')
async def delete_appointment(id:str):
    """
    Deletes an appointment with given id
    :param id: _id of the appointment
    :return: status
    """
    status = Repository.delete_appointment(id)

    return status

@router.get('/appointment/delete')
async def get_appointments(filter:dict):
    """
    Returns a list of appointments
    :param appointment: dictionary containing appointment details
    :return: status
    """
    appointments = Repository.get_appointments(filter)

    return appointments

