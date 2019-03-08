from django.urls import path, include
from . import views
# KEY: For images
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('allwikientries/', views.all_wiki_entries, name='allwikientries'),
    path('mywikientries/', views.my_wiki_entries, name='mywikientries'),
    path('create/', views.create_wiki_entry, name='create_wiki_entry'),
    path('read/<int:entry_id>', views.read_wiki_entry, name='read_wiki_entry'),
    path('update/<int:entry_id>', views.update_wiki_entry, name='update_wiki_entry'),
    path('delete/<int:entry_id>', views.delete_wiki_entry, name='delete_wiki_entry'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, })

]

# Include Authentication Modules
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
