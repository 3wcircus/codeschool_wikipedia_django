from django.contrib import admin

from .models import WikiPost, WikiPostLineItem

admin.site.register(WikiPost)
admin.site.register(WikiPostLineItem)