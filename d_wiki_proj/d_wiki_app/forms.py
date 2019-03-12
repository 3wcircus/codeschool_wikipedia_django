from django.forms import ModelForm

from .models import WikiPost


class WikiPostForm(ModelForm):
    class Meta:
        model = WikiPost
        fields = ['wiki_post_subject', 'wiki_post_text', 'wiki_post_image']
