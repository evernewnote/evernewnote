from django import forms
from django.utils.translation import gettext_lazy as _

from apps.core.models import TestNote


class EditRichTextNote(forms.ModelForm):
    class Meta:
        model = TestNote
        fields = ('title', 'content')
        labels = {
            'title': _(""),
            'content': _(""),
        }