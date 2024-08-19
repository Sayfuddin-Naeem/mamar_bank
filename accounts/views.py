from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.models import User

# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home')

class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    