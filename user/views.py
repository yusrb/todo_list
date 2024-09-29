from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

class LoginView(LoginView):
  template_name = 'user/login.html'
  
  def get_success_url(self) -> str:
    return reverse_lazy('base:index')
  
class RegisterView(CreateView):
  template_name = 'user/register.html'
  form_class = UserCreationForm

  def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
    if self.request.user.is_authenticated:
      return redirect('base:index')
    return super().get(request, *args, **kwargs)

  def get_success_url(self) -> str:
    return reverse_lazy('user:login')
=======
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import CustomUserCreationForm , CustomLoginForm

class LoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = CustomLoginForm
  
    def get_success_url(self) -> str:
        return reverse_lazy('base:index')
  
class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = CustomUserCreationForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect('base:index')
        return super().get(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy('user:login')
>>>>>>> e8ba150 (Updated)
