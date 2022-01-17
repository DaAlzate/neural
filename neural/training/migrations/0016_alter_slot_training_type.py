# Generated by Django 3.2.10 on 2022-01-17 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0015_alter_slot_training_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='training_type',
            field=models.CharField(choices=[('FUNCIONAL_TRAINING', 'Funcional Training'), ('GAP_MMSS', 'GAP/MMSS'), ('CARDIO_STEP', 'Cardio Step'), ('SENIOR', 'Senior'), ('RTG', 'RTG'), ('PILATES', 'Pilates'), ('FIT_BOXING', 'Fit Boxing'), ('BALANCE', 'Balance'), ('TRX', 'TRX'), ('YOGA', 'Yoga'), ('A_FUEGO', 'A FUEGO'), ('RUMBA', 'Rumba')], default='FUNCIONAL_TRAINING', max_length=50),
        ),
    ]
