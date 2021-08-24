from django.db.models import fields
from rest_framework import  serializers
from.models import Clinic, User, PatientReservations


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name','username' ,'last_name', 'email', 'password', 'user_type',)

    
class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = '__all__'


class PatientReservationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientReservations
        fields = '__all__'


class DoctorReservationsSerializer(serializers.ModelSerializer):

    doctor_name = serializers.ReadOnlyField()
    patient_name = serializers.ReadOnlyField()

    class Meta:
        model =PatientReservations
        fields = ['clinic', 'patient_name','doctor_name']