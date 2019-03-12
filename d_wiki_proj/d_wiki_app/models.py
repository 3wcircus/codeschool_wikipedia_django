from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Main model for a Wiki Post
class WikiPost(models.Model):
    wiki_post_subject = models.CharField(max_length=200, blank=True, null=True)
    wiki_post_text = models.TextField(max_length=5000)
    wiki_post_image = models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%d/")
    wiki_post_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.wiki_post_subject


# Model for Wki post additional details
class WikiPostLineItem(models.Model):
    wiki_post_lineitem_title = models.CharField(max_length=200, blank=True, null=True)
    wiki_post_lineitem_text = models.TextField(max_length=1000)
    wiki_post_lineitem_image = models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%d/")
    wiki_post_lineitem_wikipost = models.ForeignKey(WikiPost, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.wiki_post_lineitem_title