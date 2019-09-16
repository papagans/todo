from webapp.models import Todo
from webapp.forms import TodoForm
from webapp.models import status_choices
from django.shortcuts import render, get_object_or_404, redirect


def todo_index(request, *args, **kwargs):
    todos = Todo.objects.all()
    return render(request, 'todo_index.html', context={
        'todos': todos,
    })


def todo_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo.html', context={
        'todo': todo
    })


def todo_create_view(request):
    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'todocreate.html', context={'form': form})
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            todo = Todo.objects.create(description=data['description'], status=data['status'], date=data['date'],
                                       details=data['details'])
            return redirect('todo_view', pk=todo.pk)
        else:
            return render(request, 'todocreate.html', context={'form': form})


# def todo_create_view(request, *args, **kwargs):
#     statuses = status_choices
#     if request.method == 'GET':
#         return render(request, 'todocreate.html', context={'statuses': statuses})
#     elif request.method == 'POST':
#         description = request.POST.get('description')
#         status = request.POST.get('status')
#         date = request.POST.get('date')
#         if date == '':
#             date = None
#         details = request.POST.get('details')
#         todo = Todo.objects.create(description=description, status=status, date=date, details=details)
#         return redirect('todo_view', pk=todo.pk)


# def todo_delete(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.delete()
#     return redirect('todo_index')


def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        form = TodoForm(data={'description': todo.description,
                              'details': todo.details,
                              'status': todo.status,
                              'date': todo.date
                              })
        return render(request, 'update.html', context={'form': form, 'todo': todo})
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            todo.description = data['description']
            todo.details = data['details']
            todo.status = data['status']
            todo.date = data['date']
            todo.save()
            return redirect('todo_view', pk=todo.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'todo': todo})


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'todo': todo})
    elif request.method == 'POST':
        todo.delete()
        return redirect('todo_index')


def todo_search(request):
    todo = Todo.objects.all()
    desc_pk = request.POST.get('todo_id')
    try:
        int(desc_pk)
        todo = get_object_or_404(Todo, pk=desc_pk)
    except:
        for to_do in todo:
            if to_do.description == desc_pk:
                todo = to_do
    return render(request, 'todo.html', context={'todo': todo})
