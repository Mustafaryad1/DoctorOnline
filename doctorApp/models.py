from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

USER_TYPE_CHOICES = (
     ('doctor', 'doctor'),
     ('patient', 'patient'),
)


class User(AbstractUser):
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)


class Clinic(models.Model):
    name = models.CharField(max_length=150,)
    price = models.FloatField()
    date = models.DateTimeField(auto_created=True,auto_now=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(User,related_name='clinics', on_delete=models.CASCADE)

    

class PatientReservations(models.Model):
    clinic = models.ForeignKey(Clinic,related_name='patients', on_delete=models.CASCADE)
    patient = models.ForeignKey(User,related_name='Reservations', on_delete=models.CASCADE)

    @property
    def doctor_name(self):
        return self.clinic.doctor.username
    
    @property
    def patient_name(self):
        return self.patient.username