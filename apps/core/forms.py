from django import forms
from django.utils.translation import gettext_lazy as _

from apps.core.models import TestNote, TestNotebook


class EditRichTextNote(forms.ModelForm):
    class Meta:
        model = TestNote
        fields = ('title', 'notebook', 'content')
        labels = {
            'title': _(""),
            'notebook': _(""),
            'content': _(""),
        }

    def __init__(self, user, *args, **kwargs):
        super(EditRichTextNote, self).__init__(*args, **kwargs)
        self.fields['notebook'].queryset = TestNotebook.objects.filter(user=user)
        self.fields['notebook'].empty_label = "Choose a notebook"
