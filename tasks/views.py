"""
Brian Shoemaker
2025F INF601 A Advanced Programming with Python
Mini Project 4
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm, UserRegisterForm


def home(request):
    """
    Home page view
    """
    return render(request, 'tasks/home.html')


class TaskListView(LoginRequiredMixin, ListView):
    """
    View to display list of all tasks for logged-in user
    """
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    """
    View to display task details
    """
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    View to create new tasks
    """
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update existing tasks
    """
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete tasks
    """
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Task deleted successfully!')
        return super().delete(request, *args, **kwargs)


def register(request):
    """
    User registration view
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})