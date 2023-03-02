# Generated by Django 3.2.16 on 2023-02-28 17:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesLanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('title', models.CharField(max_length=500)),
                ('service_image', models.ImageField(upload_to='header_images')),
                ('service_description', ckeditor.fields.RichTextField()),
                ('main_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='landing.maincontentheader')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
