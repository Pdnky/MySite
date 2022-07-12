from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, DetailView, UpdateView
from core.forms import LoginForm, RegistrationForm, EditProfileForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from core.models import *


class MainPage(TemplateView):
    template_name = 'core/MainPage.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        product = ProductImage.objects.filter(is_active=True, is_main=True)
        context.update({
            'products': product,
        })
        return context


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'core/MainPage.html'
    success_url = '/'

    def form_valid(self, form):
        form.auth(self.request)
        return super(LoginView, self).form_valid(LoginForm)


class RegistrationView(FormView):
    template_name = 'core/registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'core/profile.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context


class EditProfileView(UpdateView):
    template_name = 'core/profile-edit.html'
    model = get_user_model()
    form_class = EditProfileForm
    pk_url_kwarg = 'id'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(EditProfileView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Edit profile'
        })
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), pk=self.request.user.id)


class ProductPageView(TemplateView):
    template_name = 'core/product-page.html'
    model = Product
    pk_url_kwarg = 'id'

    def get_user_data(self, **kwargs):
        context = super(ProductPageView, self).get_user_data(**kwargs)
        context.update({
            'title': 'sdfsdfsdfsdfsdfsfds'
        })
        return context

# Create your views here.
