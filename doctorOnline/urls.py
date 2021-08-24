from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from doctorApp  import views

router = routers.SimpleRouter()
router.register(r'clinics', views.ClinicView)
router.register(r'reservations', views.ReservationView)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('user/<int:pk>', views.UserView.as_view(),name="user-retrieve-update"),
    path('users/', include('doctorApp.urls')),

]
