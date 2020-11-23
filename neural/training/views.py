"""Training views."""

# Django
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, FormView
from django.urls import reverse_lazy

# Models
from neural.training.models import Slot, UserTraining
from neural.training.forms import SchduleForm
from neural.training.serializers import SlotModelSerializer


class ScheduleView(LoginRequiredMixin, FormView):
    template_name = 'training/schedule.html'
    form_class = SchduleForm
    success_url = reverse_lazy('users:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        now = timezone.localtime()
        date = timezone.localdate()
        gap_acceptance = now + timedelta(minutes=20)
        slots = Slot.objects.filter(date=date, hour_init__gte=gap_acceptance).order_by('hour_init').distinct('hour_init')

        kwargs['user'] = self.request.user
        kwargs['slots'] = SlotModelSerializer(slots, many=True).data

        return kwargs
    
    def get_success_url(self):
        success_url = super().get_success_url()
        return success_url


class MyScheduleView(LoginRequiredMixin, TemplateView):
    template_name = 'training/my_schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.localtime()
        context['user_slots'] = UserTraining.objects.filter(
            user=self.request.user,
            slot__date__gte=now
            ).order_by('slot__date')[:7]
        return context


class InfoView(LoginRequiredMixin, TemplateView):
    template_name = 'training/info.html'
