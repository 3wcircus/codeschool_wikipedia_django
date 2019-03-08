from django.db import models


class WikiPost(models.Model):
    wiki_post_subject = models.CharField(max_length=200, blank=True,null=True)
    wiki_post_text = models.TextField(max_length=5000)
    wiki_post_image = models.ImageField(blank=True, null=True, upload_to="images/%D/")

    def __str__(self):
        return self.wiki_post_subject
