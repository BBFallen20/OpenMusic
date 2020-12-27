from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from OpenMusic.settings import DEFAULT_FROM_EMAIL
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.views.generic import DetailView, CreateView
from tracks.models import Track
from .forms import TrackForm, ProfileForm
from .models import UserProfile
from django.views.generic.edit import FormMixin


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return f'{self.success_url}?slug={self.object.slug}'


class UserProfileSearchView(DetailView):
    template_name = 'account/user_search.html'
    model = UserProfile

    def get_object(self, queryset=None):
        return UserProfile.objects.get(User__username=self.kwargs.get('name', None))

    def get_context_data(self, **kwargs):
        context = super(UserProfileSearchView, self).get_context_data()
        context['published'] = Track.objects.filter(pub_by__userprofile__id=self.object.id)
        return context


class UserProfileView(DetailView, CustomSuccessMessageMixin, FormMixin):
    model = UserProfile
    template_name = 'account/user_profile.html'
    form_class = ProfileForm
    success_msg = 'Successful saved.'

    def get_object(self, queryset=None):
        username = self.kwargs.get('name', None)
        if username:
            return UserProfile.objects.get(User=username)
        if UserProfile.objects.filter(User=self.request.user):
            return UserProfile.objects.get(User=self.request.user)
        else:
            return UserProfile.objects.create(User=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        current_profile = UserProfile.objects.get(User=self.request.user)
        current_profile.description = form.cleaned_data['description']
        current_profile.image = form.cleaned_data['image']
        current_profile.save(force_update=True)
        return super().form_valid(form)


class TrackAddView(CreateView):
    model = Track
    form_class = TrackForm
    template_name = 'account/track_add.html'

    def form_valid(self, form):
        form.instance.pub_by = self.request.user
        return super(TrackAddView, self).form_valid(form)


@receiver(user_signed_up)
def user_signed_up(request, user, **kwargs):
    send_mail('Signup OpenMusic', 'Hi!\nThanks for signup!\nConfirm your email at next letter.\n OpenMusic.', DEFAULT_FROM_EMAIL, [user.email], fail_silently=True)

