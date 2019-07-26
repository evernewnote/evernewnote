from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from apps.accounts.models import User

from apps.core.forms import EditRichTextNote
from apps.core.models import Note, Notebook


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


# def edit_note(request):
#     context = {}
#     return render(request, "pages/note_edit.html", context)


def print_user_notes(user):
    notes = Note.objects.filter(user=user)
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


def new_note(request, notebook_menu_id=None):
    user = User.objects.get(username=request.user)
    notebooks = Notebook.objects.filter(user=user)
    if notebook_menu_id:
        note_sidebar_notebook = Notebook.objects.get(id=notebook_menu_id)
    else:
        note_sidebar_notebook = Notebook.objects.get(id=1)

    if request.method == 'POST':
        form = EditRichTextNote(user, request.POST)

        form, note_id = note_change(form, user)
        return redirect('/edit_note/' + str(note_id))

    else:
        form = EditRichTextNote(user=user, initial={"title": "Title"})
        context = {
            'form': form,
            'notebooks': notebooks,
            'note_sidebar_notebook': note_sidebar_notebook,
        }
        return render(request, "pages/test_note_new.html", context)


# TODO: logged in only
def edit_note(request, note_id, notebook_menu_id=None):
    note = Note.objects.get(id=note_id)
    user = User.objects.get(username=request.user)
    notebooks = Notebook.objects.filter(user=user)
    print("## edit_note ##")
    print(request.GET)
    if notebook_menu_id:
        note_sidebar_notebook = Notebook.objects.get(id=notebook_menu_id)
    else:
        note_sidebar_notebook = Notebook.objects.get(id=1)

    if request.method == 'POST':
        form = EditRichTextNote(user, request.POST, instance=note)
        form = note_change(form, user)

        print("test edit note: method is post" + request.META.get('HTTP_REFERER', '/'))
        return HttpResponseRedirect('/edit_note/' + str(note_id))
    else:
        print("test edit note: " + request.method + " " + request.META.get('HTTP_REFERER', '/'))
        form = EditRichTextNote(user=user, instance=note)

        notes_by_notebook = {}
        for notebook in notebooks:
            l = []
            for n in Note.objects.filter(notebook=notebook.id):
                l.append(n)
            notes_by_notebook[notebook.title] = l

        print(notes_by_notebook)

        context = {
            'form': form,
            'note_id': note_id,
            'notebooks': notebooks,
            'note_sidebar_notebook': note_sidebar_notebook,
            'notes_by_notebook': notes_by_notebook
        }
        return render(request, "pages/test_note_edit.html", context)


def page_not_found(request):
    return render(request, "404.html")
