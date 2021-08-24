# Generated by Django 3.2.6 on 2021-08-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('doctor', 'doctor'), ('patient', 'patient')], max_length=50),
        ),
    ]
