from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ServiceRequest


# 🔧 Service Request Form
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']
        widgets = {
            'request_type': forms.TextInput(
                attrs={
                    'class': (
                        'block w-full px-4 py-3 mt-2 text-gray-700 bg-white border '
                        'border-gray-300 rounded-lg focus:outline-none focus:ring-2 '
                        'focus:ring-blue-500 focus:border-transparent'
                    )
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': (
                        'block w-full px-4 py-3 mt-2 text-gray-700 bg-white border '
                        'border-gray-300 rounded-lg focus:outline-none focus:ring-2 '
                        'focus:ring-blue-500 focus:border-transparent resize-none'
                    ),
                    'placeholder': 'Enter a detailed description of your request...',
                    'rows': 4
                }
            ),
            'attachment': forms.ClearableFileInput(
                attrs={
                    'class': (
                        'block w-full mt-2 text-sm text-gray-500 file:mr-4 file:py-2 '
                        'file:px-4 file:rounded-lg file:border-0 file:text-sm '
                        'file:font-semibold file:bg-blue-50 file:text-blue-700 '
                        'hover:file:bg-blue-100'
                    )
                }
            )
        }
        labels = {
            'request_type': 'Select Request Type',
            'description': 'Description',
            'attachment': 'Upload Attachment',
        }

    def clean_attachment(self):
        attachment = self.cleaned_data.get('attachment')
        allowed_types = ['application/pdf', 'image/jpeg', 'image/png']
        max_size = 5 * 1024 * 1024  # 5 MB

        if attachment:
            if attachment.content_type not in allowed_types:
                raise forms.ValidationError('Only PDF, JPG, and PNG files are allowed.')
            if attachment.size > max_size:
                raise forms.ValidationError('File size should not exceed 5 MB.')
        return attachment


# 🔑 Custom User Registration Form
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': (
                    'w-full px-4 py-3 mt-2 border rounded-lg focus:outline-none '
                    'focus:ring-2 focus:ring-blue-500'
                ),
                'placeholder': 'Enter your first name'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': (
                    'w-full px-4 py-3 mt-2 border rounded-lg focus:outline-none '
                    'focus:ring-2 focus:ring-blue-500'
                ),
                'placeholder': 'Enter your last name'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': (
                        'w-full px-4 py-3 mt-2 border rounded-lg focus:outline-none '
                        'focus:ring-2 focus:ring-blue-500'
                    ),
                    'placeholder': 'Enter your username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': (
                        'w-full px-4 py-3 mt-2 border rounded-lg focus:outline-none '
                        'focus:ring-2 focus:ring-blue-500'
                    ),
                    'placeholder': 'Enter your email address'
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': (
                        'w-full px-4 py-3 mt-2 border rounded-lg focus:outline-none '
                        'focus:ring-2 focus:ring-blue-500'
                    ),
                    'placeholder': 'Enter your password'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': (
                        'w-full px-4 py-3 mt-2 border rounded-lg focus:outline-none '
                        'focus:ring-2 focus:ring-blue-500'
                    ),
                    'placeholder': 'Confirm your password'
                }
            )
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


# 🔐 Custom Login Form
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': (
                    'w-full px-4 py-3 mt-2 border rounded-lg focus:outline-none '
                    'focus:ring-2 focus:ring-blue-500'
                ),
                'placeholder': 'Enter your username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': (
                    'w-full px-4 py-3 mt-2 border rounded-lg focus:outline-none '
                    'focus:ring-2 focus:ring-blue-500'
                ),
                'placeholder': 'Enter your password'
            }
        )
    )
