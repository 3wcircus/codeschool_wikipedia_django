# Generated by Django 2.1.1 on 2019-03-10 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('d_wiki_app', '0006_wikipostlineitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipostlineitem',
            name='wiki_post_lineitem_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='wikipostlineitem',
            name='wiki_post_lineitem_wikipost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='d_wiki_app.WikiPost'),
        ),
        migrations.AlterField(
            model_name='wikipost',
            name='wiki_post_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
