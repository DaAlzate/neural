"""Training admin."""

from django.contrib import admin
from neural.training.models import UserTraining, Slot, Space, ImagePopUp
from neural.training.forms import ImagePopUpForm


class UserTrainingInline(admin.TabularInline):
    model = UserTraining
    extra = 0
    autocomplete_fields = ['user']


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_filter = ['date', 'hour_init']
    list_display = ['pk', '__str__', 'date', 'hour_init', 'available_places', 'training_type']
    inlines = [UserTrainingInline]


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    pass


@admin.register(UserTraining)
class UserTrainingAdmin(admin.ModelAdmin):
    list_display = ['user', 'slot', 'status']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']


@admin.register(ImagePopUp)
class ImagePopUpAdmin(admin.ModelAdmin):
    list_display = ["image_name", "image", "is_active"]
    form = ImagePopUpForm
