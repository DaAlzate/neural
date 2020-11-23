# Generated by Django 3.0.11 on 2020-11-23 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20201123_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertraining',
            name='space',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_trainings', to='training.Space'),
            preserve_default=False,
        ),
    ]
