# Generated by Django 3.2.6 on 2021-08-24 22:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctorApp', '0002_auto_20210824_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctorApp.user'),
            preserve_default=False,
        ),
    ]
