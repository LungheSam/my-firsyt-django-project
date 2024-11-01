from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TodoList
from todolist_app.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    # return HttpResponse("<h1>Welcome to the Party of todo list</h1>")
    # context={
    #     'welcome_text': 'Welcome to the Party of todo list'
    #     }
    # return render(request,'todolist_app/home.html',context)

    if request.method == 'POST':
        form=TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully')
        return redirect('home-todo')
    else:
        alltasks=TodoList.objects.all()
        paginator = Paginator(alltasks, 5)
        page_number = request.GET.get('page',1)
        alltasks=paginator.get_page(page_number)
        context={
            'alltasks':alltasks,
            'edit':False
        }
        return render(request,'todolist_app/home.html',context)
def tasks(request):
    return render(request,'todolist_app/todolist.html')
def contact(request):
    context={
        'phone':'+256742618584'
    }
    return render(request,"todolist_app/contactus.html",context)



def delete_task(request,id):
    task_to_delete = TodoList.objects.get(id=id)
    task_to_delete.delete()
    return redirect ("home-todo")

def edit_task(request, id):
    # task_to_edit = TodoList.objects.get(id=id)
    # form = TaskForm(instance=task_to_edit)

    if request.method == 'POST':
        task=TodoList.objects.get(id=id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Edited Successfully')
        return redirect('home-todo')
    else:
        task_to_edit=TodoList.objects.get(id=id)
        alltasks=TodoList.objects.all()
        context={
            'task_object': task_to_edit,
            'edit': True,
            'alltasks': alltasks
        }
        return render(request,'todolist_app/home.html',context)
def complete_task(request,id):
    task_to_complete = TodoList.objects.get(id=id)
    task_to_complete.done=True
    task_to_complete.save()
    return redirect ("home-todo")
def pending_task(request, id):
    task_to_pending = TodoList.objects.get(id=id)
    task_to_pending.done=False
    task_to_pending.save()
    return redirect ("home-todo")
def see_developer_biography(request):
    context={
        'name':"Samuel Lunghe Putshu",
        'age':22,
        'origin':"DR Congo"
    }
    return render(request,"todolist_app/biography.html",context)


