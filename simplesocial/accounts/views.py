from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import DiagnosisInfo
from accounts.forms import DiagnosisInfoForm
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class Result(TemplateView):
    template_name='accounts/result.html'

class CreateDiagnosisView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    # redirect_field_name = 'accounts/result.html'
    # get_absolute_url='result'
    # success_url = reverse_lazy('res')
    form_class = DiagnosisInfoForm
    model = DiagnosisInfo
