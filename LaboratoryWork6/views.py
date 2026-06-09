from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from .models import Car, Employee, Department, Device, Post, Book, Author, Category, Article

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(is_available=True, price__gt=1000000).order_by('-year')


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.get_object()
        context['colleagues'] = Employee.objects.filter(
            department=employee.department
        ).exclude(id=employee.id)
        return context


class DeviceCreateView(CreateView):
    model = Device
    fields = ['name', 'serial_number', 'purchase_date']
    template_name = 'devices/device_form.html'

    def get_success_url(self):
        current_year = timezone.now().year
        if self.object.purchase_date.year == current_year:
            return reverse('device-list')  # Предполагается наличие такого url-name
        return reverse('device-detail', kwargs={'pk': self.object.pk})

class DeviceUpdateView(UpdateView):
    model = Device
    fields = ['name', 'serial_number', 'purchase_date']
    template_name = 'devices/device_form.html'

    def get_success_url(self):
        current_year = timezone.now().year
        if self.object.purchase_date.year == current_year:
            return reverse('device-list')
        return reverse('device-detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.status == 'published':
            raise PermissionDenied("Нельзя удалить опубликованный пост!")
        return super().post(request, *args, **kwargs)


class ExtraContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BookListView(ExtraContextMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class AuthorListView(ExtraContextMixin, ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'

class CategoryArticleListView(ListView):
    model = Article
    template_name = 'blog/category_articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category, slug=category_slug)
        return Article.objects.filter(category=category)