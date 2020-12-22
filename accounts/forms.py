from django import forms
from tracks.models import Track


class TrackForm(forms.ModelForm):
    widgets = {
        'pub_by': forms.HiddenInput
    }

    class Meta:
        model = Track
        fields = ('title', 'description', 'audio', 'genre', 'author')




