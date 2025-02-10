# Generated by Django 4.2.6 on 2025-01-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointments_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='scheduled', max_length=10),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='organisation',
            field=models.CharField(max_length=255, verbose_name='Организация'),
        ),
    ]
