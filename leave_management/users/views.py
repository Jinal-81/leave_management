from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .constants import HOD_NAME_LABEL, HOD_WELCOME_MSG, STAFF_NAME_LABEL, STAFF_WELCOME_MSG
from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    """
    view for the user registration.
    """
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    """
    view for the user login
    """
    template_name = 'users/login.html'
    success_url = reverse_lazy('dashboard')


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    view for the dashboard after user login.
    """
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Check if user is an HOD
        if user.is_hod():
            context['dashboard_role'] = HOD_NAME_LABEL
            context['dashboard_message'] = HOD_WELCOME_MSG

        # Check if user is staff
        elif user.is_staff():
            context['dashboard_role'] = STAFF_NAME_LABEL
            context['dashboard_message'] = STAFF_WELCOME_MSG

        return context


class LogoutView(View):
    """
    view for the user logout, after logout user will be redirect to the login view
    """
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

