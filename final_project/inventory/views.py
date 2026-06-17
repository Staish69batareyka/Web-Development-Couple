from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Count

from .models import Device
from .forms import CustomUserCreationForm, DeviceForm

class ExtraContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['server_time'] = timezone.now()
        return context

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('device-list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class DeviceListView(LoginRequiredMixin, ExtraContextMixin, ListView):
    model = Device
    template_name = 'inventory/device_list.html'
    context_object_name = 'devices'  # Условие задачи №5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        status_filter = self.request.GET.get('status', '')

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset


class DeviceDetailView(LoginRequiredMixin, DetailView):
    model = Device
    template_name = 'inventory/device_detail.html'
    slug_url_kwarg = 'category_slug'
    context_object_name = 'device'


class DeviceCreateView(LoginRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'inventory/device_form.html'

    def get_success_url(self):
        current_year = timezone.now().year
        if self.object.purchase_date.year == current_year:
            return reverse_lazy('device-list')
        return reverse_lazy('device-detail', kwargs={'category_slug': self.object.slug})


class DeviceUpdateView(LoginRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'inventory/device_form.html'
    slug_url_kwarg = 'category_slug'

    def get_success_url(self):
        send_mail(
            subject='Изменение данных оборудования',
            message=f'Сотрудник {self.request.user.username} отредактировал запись: {self.object.name}.',
            from_email='system@warehouse.local',
            recipient_list=['admin@warehouse.local']
        )
        current_year = timezone.now().year
        if self.object.purchase_date.year == current_year:
            return reverse_lazy('device-list')
        return reverse_lazy('device-detail', kwargs={'category_slug': self.object.slug})


class DeviceDeleteView(LoginRequiredMixin, DeleteView):
    model = Device
    template_name = 'inventory/device_confirm_delete.html'
    slug_url_kwarg = 'category_slug'
    success_url = reverse_lazy('device-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.status == 'active':
            return render(request, self.template_name, {
                'object': self.object,
                'error': "Критическая ошибка: Нельзя удалить работающее оборудование!"
            })
        return super().post(request, *args, **kwargs)


class ReportView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = Device.objects.count()
        status_counts = Device.objects.values('status').annotate(count=Count('status'))

        report_data = []
        for item in status_counts:
            percentage = (item['count'] / total * 100) if total > 0 else 0
            status_display = dict(Device.STATUS_CHOICES).get(item['status'])
            report_data.append({
                'status': status_display,
                'count': item['count'],
                'percentage': int(percentage)
            })

        context['report_data'] = report_data
        context['total'] = total
        return context