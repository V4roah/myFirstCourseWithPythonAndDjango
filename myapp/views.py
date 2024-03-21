from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    title = "Django Course!!!"
    return render(request, "index.html", {
        "title": title
    })


def about(request):
    username = "v4roah"
    return render(request, "about.html", {
        "username": username
    })


def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}</h1>")
    # return HttpResponse ("<h1>Hello %s</h1>" % username) #Es otra manera de manejar strings


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": projects
    })


def tasks(request):
    # # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, title=title) #Se usa esta manera importando el get_object_or_404 de django.shortcuts para que me aparezca un mensaje de error si no encuentra un id, sale un error de page not found 404
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {
            "form": CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/tasks/')


def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {
            "form": CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')
