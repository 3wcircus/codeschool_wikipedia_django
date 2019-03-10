from django.shortcuts import render, redirect
# import the logging library
import logging

# Get an instance of a logger
from .forms import WikiPostForm
from .models import WikiPost

logger = logging.getLogger(__name__)


# This will be the default page listing all entries
def all_wiki_entries(request):
    logger.debug('All Entries')
    wiki_entries = WikiPost.objects.all()

    return render(request, 'd_wiki_app/wiki_entries.html', {'wiki_entries': wiki_entries})


# This view will just return the logged in users entries
def my_wiki_entries(request):
    logger.debug('My Entries')
    return render(request, 'd_wiki_app/base.html')


# Default landing page
def index(request):
    logger.info('Index')
    return render(request, 'd_wiki_app/base.html')


# Create a new entry
def create_wiki_entry(request):
    logger.debug('create_wiki_entry')
    new_post_form = WikiPostForm(request.POST or None, request.FILES or None)
    if new_post_form.is_valid():
        new_post_form.save()
        return redirect('allwikientries')
    return render(request, 'd_wiki_app/wiki_entry.html', {'wiki_form': new_post_form})


# Display a an entry
def read_wiki_entry(request, entry_id):
    logger.debug('read_wiki_entry')
    return render(request, 'd_wiki_app/wiki_entries.html')


# Edit an entry
def update_wiki_entry(request, entry_id):
    entry = WikiPost.objects.get(pk=entry_id)
    new_post_form = WikiPostForm(request.POST or None, request.FILES or None, instance=entry)
    if new_post_form.is_valid():
        new_post_form.save()
        return redirect('allwikientries')
    return render(request, 'd_wiki_app/wiki_entry.html', {'wiki_form': new_post_form})


# Delete an entry
def delete_wiki_entry(request, entry_id):
    logger.debug('delete_wiki_entry')
    return render(request, 'd_wiki_app/wiki_entries.html')
