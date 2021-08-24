from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Clinic, User, PatientReservations
from .serializers import (PatientReservationsSerializer,
                          UserSerializer,
                          ClinicSerializer,
                          DoctorReservationsSerializer)
from .permissions import IsPatient, IsProfileOwner,IsDoctor


class UserView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsProfileOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClinicView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsDoctor]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class ReservationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PatientReservations.objects.all()
    serializer_class = PatientReservationsSerializer

    def get_serializer_class(self):
        if self.action in ["list"]:
            return DoctorReservationsSerializer
        return super().get_serializer_class()


# Auth Views : Register
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
    
        serializer.is_valid(raise_exception=False)
        try:
            user = User.objects.get(username=request.data.get("username"))
        except Exception as e:
            return Response({"success":False, "message":"Please enter valid credential"})
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'user_type':user.user_type
        })


# Auth Views : Login
@api_view(['POST'])
def register(request):
    """
    Saves a new user on the database
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'success':True}, status=status.HTTP_201_CREATED, headers=serializer.data)
            except Exception as e :
                
                return Response({"errors":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)
