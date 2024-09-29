from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  DeleteView,
  DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from typing import Any
from .models import Task
from .forms import TaskForm

class BaseListView(ListView):
  model = Task
  context_object_name = 'tasks'

  def get_context_data(self, **kwargs) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      if self.request.user.is_authenticated:
        context["tasks"] = context['tasks'].filter(user = self.request.user)
        if context['tasks'].filter(complete = False).count() == 0:
          context['count'] = '0'
        else :
           context['count'] = context['tasks'].filter(complete = False).count()
      else :
         context['null'] = 'Belum ada Postingan'

      search_input = self.request.GET.get('search-value') 
      if search_input:
         context['tasks'] = context['tasks'].filter(judul__icontains = search_input)
      return context
  
  
class BaseCreateView(LoginRequiredMixin , CreateView):
  model = Task
  form_class = TaskForm

  def get_context_data(self, **kwargs) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context["judul"] = "Create Form"
      context["submit"] = "Create"
      return context
  
  def form_valid(self, form):
      if self.request.user.is_authenticated:
        form.instance.user = self.request.user
      return super().form_valid(form)
  

  def get_success_url(self) -> str:
    return reverse_lazy('base:index')

class BaseUpdateView(LoginRequiredMixin , UpdateView):
  model = Task
  form_class = TaskForm

  def get_context_data(self, **kwargs) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context["judul"] = "Update Form"
      context["submit"] = "Update"
      return context

  def get_success_url(self) -> str:
    return reverse_lazy('base:index')
  
class BaseDetailView(LoginRequiredMixin , DetailView):
   model = Task
   context_object_name = 'task'

   def get_context_data(self, **kwargs) -> dict[str, Any]:
       task_lain = self.model.objects.exclude(id = self.object.id)
       context = super().get_context_data(**kwargs)
       context["task_lain"] = task_lain
       return context
   
class BaseDeleteView(LoginRequiredMixin , DeleteView):
   model = Task
   context_object_name = 'task'

   def get_success_url(self) -> str:
      return reverse_lazy('base:index')