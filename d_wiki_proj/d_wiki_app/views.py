from django.shortcuts import render, redirect, get_object_or_404
# import the logging library
import logging

# Get an instance of a logger
from .forms import WikiPostForm
from .models import WikiPost

logger = logging.getLogger(__name__)


# This will be the default page listing all entries
def all_wiki_entries(request):
    print('All Entries')
    wiki_entries = WikiPost.objects.all()

    return render(request, 'd_wiki_app/wiki_entries.html', {'wiki_entries': wiki_entries})


# This view will just return the logged in users entries
def my_wiki_entries(request):
    print('My Entries')
    wiki_entries = WikiPost.objects.filter(wiki_post_user=request.user)
    return render(request, 'd_wiki_app/wiki_entries.html', {'wiki_entries': wiki_entries})


# Default landing page
def index(request):
    logger.info('Index')
    return render(request, 'd_wiki_app/base.html')


# Create a new entry
def create_wiki_entry(request):
    print('create_wiki_entry')
    new_post_form = WikiPostForm(request.POST or None, request.FILES or None)
    if new_post_form.is_valid():
        new_post_form.save()
        return redirect('allwikientries')
    return render(request, 'd_wiki_app/wiki_entry_create.html', {'wiki_form': new_post_form})


# Display a an entry
def read_wiki_entry(request, entry_id):
    print('read_wiki_entry')
    entry = get_object_or_404(WikiPost, pk=entry_id)
    return render(request, 'd_wiki_app/wiki_entry.html', {'entry': entry})


# Edit an entry
def update_wiki_entry(request, entry_id):
    entry = WikiPost.objects.get(pk=entry_id)
    new_post_form = WikiPostForm(request.POST or None, request.FILES or None, instance=entry)
    if new_post_form.is_valid():
        new_post_form.save()
        return redirect('allwikientries')
    return render(request, 'd_wiki_app/wiki_entry_edit.html', {'wiki_form': new_post_form})


# Delete an entry
def delete_wiki_entry(request, entry_id):
    print('delete_wiki_entry')
    entry = get_object_or_404(WikiPost, pk=entry_id)
    if request.method == 'POST':
        print('Removing Post')
        entry.delete()
        return redirect('allwikientries')
    return render(request, 'd_wiki_app/wiki_entry_delete.html', {'entry': entry})
