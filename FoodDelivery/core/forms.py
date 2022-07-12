from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput())

    def clean(self):
        user = get_user_model().objects.filter(
            username=self.cleaned_data['username']
        ).first()

        if not user or not user.check_password(self.cleaned_data['password']):
            raise forms.ValidationError('Неправильный логин или пароль')

    def auth(self, request):
        user = authenticate(request, **self.cleaned_data)
        login(request, user)
        return user


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    check_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )

    def clean_check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['check_password']:
            raise forms.ValidationError('Pass don\'t match')
        return self.cleaned_data['check_password']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class EditProfileForm(forms.ModelForm):

        class Meta:
            model = get_user_model()
            fields = '__all__'
            exclude = (
                'password',
                'last_login',
                'is_active',
                'is_superuser',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
                'date_joined',
                'bonus_coin'
            )




