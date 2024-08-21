from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Todo
from django.http import HttpResponse
import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TodoForm 
from django.http import HttpResponseForbidden

# Create your views here.


# @login_required
def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
            return render(request, 'projects/login.html', {'error_message': error_message})
    else:
        return render(request, 'projects/login.html')  


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # It shows "Successfully registered." If your registration was successful
            messages.success(request, 'Successfully registered. Please log in.') 
            return redirect('login')
        else:
            return render(request, 'projects/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()

    return render(request, 'projects/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Project.objects.create(title=title)
        return redirect('home')
    return render(request, 'projects/create_project.html')


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    return render(request, 'projects/delete_project.html', {'project': project})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/view_project.html', {'project': project})


def edit_project_title(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    new_title = request.POST.get('title')
    if new_title:
        project.title = new_title
        project.save()
    return redirect('project_detail', project_id=project_id)


def create_todo(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description')
        Todo.objects.create(project=project, title=title, description=description)
        return redirect('project_detail', project_id=project_id)
    return render(request, 'projects/create_todo.html', {'project': project})


def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    project_id = todo.project.pk

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        status = request.POST.get('status') == 'on'

        if title and description:
            todo.title = title
            todo.description = description
            todo.status = status
            todo.save()
            return redirect('home')
        else:
            error_message = "Title and description are required."
            return render(request, 'projects/update_todo.html', {'todo': todo, 'error_message': error_message})
    return render(request, 'projects/update_todo.html', {'todo': todo})


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    project_id = todo.project.pk
    
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'projects/delete_todo.html', {'todo': todo})


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        if 'update' in request.POST:
            return redirect('update_todo', pk=todo.pk)
        elif 'delete' in request.POST:
            return redirect('delete_todo', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    
    context = {
        'todo': todo,
        'form': form,
    }
    return render(request, 'projects/todo_detail.html', context)


def export_gist(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    completed_todos = project.todos.filter(status=True)
    pending_todos = project.todos.filter(status=False)
    summary = f"Summary: {completed_todos.count()}/{project.todos.count()} todos completed\n"
    pending_section = "\n## Pending\n" + "\n".join([f"- [ ] {todo.title}" for todo in pending_todos])
    completed_section = "\n## Completed\n" + "\n".join([f"- [x] {todo.title}" for todo in completed_todos])
    content = f"# {project.title}\n\n{summary}{pending_section}{completed_section}"

    # Save the markdown file locally
    file_path = f"{project.title}.md"
    with open(file_path, 'w') as file:
        file.write(content)

    # Post the content to GitHub as a secret gist
    response = requests.post('https://api.github.com/gists', json={
        "files": {f"{project.title}.md": {"content": content}},
        "public": False
    }, headers={'Authorization': f'token {settings.GITHUB_TOKEN}'})
    
    gist_url = response.json().get('html_url', 'Error creating gist')  
    return HttpResponse(f"Exported Gist URL: {gist_url}. Local file saved as {file_path}")
