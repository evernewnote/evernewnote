from django.shortcuts import render
from django import forms

from apps.core.models import TestNote


class EditRichTextNote(forms.ModelForm):
    class Meta:
        model = TestNote
        fields = '__all__'


# Two example views. Change or delete as necessary.
def home(request):
    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


def user_page(request):
    context = {}
    return render(request, "", context)


# TODO: logged in only
def main_view(request):
    context = {}
    return render(request, "pages/main.html", context)


# TODO: logged in only
def edit_note(request):
    context = {}
    return render(request, "pages/note_edit.html", context)


def test_edit_note(request):
    form = EditRichTextNote()
    context = {
        'form': form
    }
    return render(request, "pages/test_note_edit.html", context)