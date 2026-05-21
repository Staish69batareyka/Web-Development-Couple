from django.db import models

class BaseModelName(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Doctor(BaseModelName):

    # name = models.CharField(max_length=100, verbose_name="Doctor's Name")
    speciality = models.CharField(max_length=100, verbose_name="Doctor's Speciality")

    def __str__(self):
        return self.name

class Treatment(BaseModelName):
    # treatment_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(BaseModelName):

    # name = models.CharField(max_length=100, verbose_name="Patient's Name")
    age = models.IntegerField(verbose_name='Patient Age')
    contact_info = models.CharField(max_length=255, verbose_name="Patient's Contacts")

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='patient'
    )

    treatment = models.ManyToManyField(
        Treatment,
        through='PatientTreatment', #?
        verbose_name='treatment '

    )

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    record_details = models.TextField()

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='patient'
    )

    def __str__(self):
        return self.record_details

class PatientTreatment(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='patient'
    )
    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.CASCADE,
        verbose_name='treatment'
    )
    date_started = models.DateField(auto_now_add=True, verbose_name='date_started')
    notes = models.TextField(null=True, blank=True, verbose_name='notes')

    def __str__(self):
        return self.notes