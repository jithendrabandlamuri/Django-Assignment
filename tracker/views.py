from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Task
from .forms import Add_Task
from django.urls import reverse_lazy

def base_page(request):
    return render(request,'base.html',{})

class AddPost(CreateView):
    model=Task
    form_class = Add_Task
    template_name = 'addpost.html'

class Updat_task(UpdateView):
    model=Task
    template_name = 'update_task.html'
    fields = ['add_task','Progress']
    success_url = reverse_lazy('view')

class Delete_task(DeleteView):
    model=Task
    template_name = 'delete.html'
    fields = ['add_task','Progress']
    success_url = reverse_lazy('view')


def list_view(request):
    data=Task.objects.filter(author=request.user)
    return render(request,'taskview.html',{'data':data})


