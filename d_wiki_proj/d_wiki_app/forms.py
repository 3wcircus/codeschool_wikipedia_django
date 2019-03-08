from django.forms import ModelForm

from .models import WikiPost


class WikiPostForm(ModelForm):
    class Meta:
        model = WikiPost
        fields = '__all__'

