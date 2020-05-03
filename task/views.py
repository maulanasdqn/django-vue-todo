from django.shortcuts import render
from django.views.generic import View
from .models import Task
from django.shortcuts import redirect
from .form import TaskForm
from django.http import JsonResponse
from django.forms.models import model_to_dict

class TaskView(View):
    def get(self, request):
        tasks = list(Task.objects.values())

        if request.is_ajax():
            return JsonResponse({'tasks':tasks}, status=200)

        return render(request, 'task/tasks.html', context={'name': 'RED'})


    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            baru = form.save()
            return JsonResponse({'task': model_to_dict(baru)}, status=200)
        return redirect(task)

class Taskberes(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.completed = True
        task.save()
        return JsonResponse({'task': model_to_dict(task)}, status=200)

class hapus(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'result': 'ok'}, status=200)
