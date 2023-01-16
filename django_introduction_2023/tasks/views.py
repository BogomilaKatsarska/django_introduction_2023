from django.shortcuts import render
from django import http

from django_introduction_2023.tasks.models import Task


def index(request):
    return http.HttpResponse('It works')


def get_all_tasks(request):
    all_tasks = Task.objects.order_by('id').all()
    result = ', '.join(f'{t.name} ({t.id})' for t in all_tasks)
    return http.HttpResponse(result)


def index2(request):
    all_tasks = Task.objects.order_by('id').all()
    context = {
        'title': 'The tasks app',
        'tasks': all_tasks,
    }
    return render(request, 'index2.html', context)
