from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from apps.accounts.models import User

from apps.core.forms import EditRichTextNote
from apps.core.models import TestNote


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


def test_new_note(request):
    if request.method == 'POST':
        form = EditRichTextNote(request.POST)
        user = User.objects.get(username=request.user)

        form, note_id = note_change(form, user)
        return redirect('/test_edit_note/' + str(note_id))

    else:
        form = EditRichTextNote(initial={"title": "Title"})
        context = {
            'form': form
        }
        return render(request, "pages/test_note_new.html", context)


def test_edit_note(request, note_id):
    note = TestNote.objects.get(id=note_id)
    print("#########################")
    if request.method == 'POST':
        form = EditRichTextNote(request.POST, instance=note)
        user = User.objects.get(username=request.user)

        form = note_change(form, user)
        print("test edit note: method is post" + request.META.get('HTTP_REFERER', '/'))
        return HttpResponseRedirect('/test_edit_note/' + str(note_id))
    else:
        print("test edit note: " + request.method + " " + request.META.get('HTTP_REFERER', '/'))
        form = EditRichTextNote(instance=note)

        context = {
            'form': form,
            'note_id': note_id,
        }
        return render(request, "pages/test_note_edit.html", context)


def nothing(request):
    print(request.method)
    print(request.META)
    print(request.get_full_path)
    print(request.get_full_path_info)
    context = {}
    return render(request, "pages/empty.html", context)