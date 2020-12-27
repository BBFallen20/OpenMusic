from django import forms
from tracks.models import Track
from .models import UserProfile


class TrackForm(forms.ModelForm):
    widgets = {
        'pub_by': forms.HiddenInput
    }

    class Meta:
        model = Track
        fields = ('title', 'description', 'audio', 'genre', 'author')


class ProfileForm(forms.ModelForm):
    widgets = {
        'User': forms.HiddenInput
    }

    class Meta:
        model = UserProfile
        fields = ('image', 'description')




