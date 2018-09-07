from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class SnippetExtension(PageExtension):
    name = models.CharField(max_length=255)
    snippets = models.ManyToManyField('Snippet')

    def copy_relations(self, oldinstance, language):
        for snippet in oldinstance.snippets.all():
            snippet.pk = None
            snippet.mypageextension = self
            snippet.save()


extension_pool.register(SnippetExtension)


class Snippet(models.Model):
    code = models.TextField()
