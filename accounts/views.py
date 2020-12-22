from django.core.mail import send_mail
from OpenMusic.settings import DEFAULT_FROM_EMAIL
from allauth.account.signals import user_signed_up, email_confirmed
from django.dispatch import receiver
from django.views.generic import TemplateView, CreateView
from tracks.models import Track
from .forms import TrackForm


class UserProfileView(TemplateView):
    template_name = 'account/user_profile.html'


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

