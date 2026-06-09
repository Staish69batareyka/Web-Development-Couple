from django.core.exceptions import ObjectDoesNotExist
from appointments.models import Patient, Doctor, Treatment

def get_patient_info(patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        return f"Пациент: {patient.name}, Лечащий врач: {patient.doctor.name}"

    except Patient.DoesNotExist:
        return f"Ошибка: Пациент с ID {patient_id} не зарегистрирован в системе"

    except Patient.MultipleObjectsReturned:
        return "Ошибка: Найдено более одного пациента с такими данными"

def count_young_patients(min_age):
    count = Patient.objects.filter(age__lt=min_age).count()
    return f"Найдено {count} пациентов младше {min_age} лет"

def get_doctors_by_specialty(exclude_specialty):
    doctors = Doctor.objects.exclude(speciality=exclude_specialty).order_by('name')

    for doc in doctors:
        print(f"Врач: {doc.name} | Специализация: {doc.speciality}")

def ensure_treatment_exists(name):
    if Treatment.objects.filter(name=name).exists():
        print(f"Лечение {name} уже есть в базе")
    else:
        Treatment.objects.create(name=name)
        print(f"Запись {name} успешно создана")


def rename_specialty(old_name, new_name):
    updated_count = Doctor.objects.filter(speciality=old_name).update(speciality=new_name)
    return updated_count


def get_patient_names():
    names_list = Patient.objects.values_list('name', flat=True)
    return list(names_list)