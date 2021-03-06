# Generated by Django 3.2.6 on 2021-08-24 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorApp', '0003_clinic_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientreservations',
            name='clinic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='doctorApp.clinic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientreservations',
            name='patient',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Reservations', to='doctorApp.clinic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clinic',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinics', to=settings.AUTH_USER_MODEL),
        ),
    ]
