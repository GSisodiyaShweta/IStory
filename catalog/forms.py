from django.forms import ModelForm
from catalog.models import Player
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class PlayerEntryForm(ModelForm):
    class Meta:
        model = Player
        fields = ["your_name", "your_email"]
        labels = {'your_name': _('Name'),
                  'your_email': _('Email')}

    def save(self, commit=True):
        player = super(PlayerEntryForm, self).save(commit=False)
        player.your_name = self.cleaned_data["your_name"]
        player.your_email = self.cleaned_data["your_email"]
        if commit:
            player.save()
        return player
