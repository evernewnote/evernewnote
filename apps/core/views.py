from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from apps.accounts.models import User

from apps.core.forms import EditRichTextNote
from apps.core.models import TestNote, TestNotebook


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


def print_user_notes(user):
    notes = TestNote.objects.filter(user=user)
    for note in notes:
        print(note)


def note_change(form, user):
    if form.is_valid():
        note = form.save(commit=False)
        note.user = user
        note.save()
        print_user_notes(user)
        return form, note.id
    else:
        return None


def test_new_note(request, notebook_menu_id=None):
    user = User.objects.get(username=request.user)
    notebooks = TestNotebook.objects.filter(user=user)
    if notebook_menu_id:
        note_sidebar_notebook = TestNotebook.objects.get(id=notebook_menu_id)
    else:
        note_sidebar_notebook = TestNotebook.objects.get(id=1)

    if request.method == 'POST':
        form = EditRichTextNote(user, request.POST)

        form, note_id = note_change(form, user)
        return redirect('/test_edit_note/' + str(note_id))

    else:
        form = EditRichTextNote(user=user, initial={"title": "Title"})
        context = {
            'form': form,
            'notebooks': notebooks,
            'note_sidebar_notebook': note_sidebar_notebook,
        }
        return render(request, "pages/test_note_new.html", context)


def test_edit_note(request, note_id, notebook_menu_id=None):
    note = TestNote.objects.get(id=note_id)
    user = User.objects.get(username=request.user)
    notebooks = TestNotebook.objects.filter(user=user)
    print("## test_edit_note ##")
    print(request.GET)
    if notebook_menu_id:
        note_sidebar_notebook = TestNotebook.objects.get(id=notebook_menu_id)
    else:
        note_sidebar_notebook = TestNotebook.objects.get(id=1)

    if request.method == 'POST':
        form = EditRichTextNote(user, request.POST, instance=note)
        form = note_change(form, user)

        print("test edit note: method is post" + request.META.get('HTTP_REFERER', '/'))
        return HttpResponseRedirect('/test_edit_note/' + str(note_id))
    else:
        print("test edit note: " + request.method + " " + request.META.get('HTTP_REFERER', '/'))
        form = EditRichTextNote(user=user, instance=note)

        context = {
            'form': form,
            'note_id': note_id,
            'notebooks': notebooks,
            'note_sidebar_notebook': note_sidebar_notebook,
        }
        return render(request, "pages/test_note_edit.html", context)


def choose_notebook(request, notebook):
    print("Choose " + str(notebook))
    return redirect(request.META.get('HTTP_REFERER', '/'), notebook_menu_id=notebook)


def page_not_found(request):
    return render(request, "404.html")
