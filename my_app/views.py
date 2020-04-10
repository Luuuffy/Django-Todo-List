from django.shortcuts import render
from django.utils import timezone
from.models import Todo
from django.http import HttpResponseRedirect


def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'my_app/index.html', {"todo_items":todo_items})


def add_todo(request):
    item = request.POST.get('Item')
    item_date = timezone.now()
    Todo.objects.create(text=item, added_date=item_date)
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    to_delete = Todo.objects.filter(id=todo_id)
    to_delete.delete()
    return HttpResponseRedirect("/")
