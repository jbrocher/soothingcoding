from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class SnippetExtension(PageExtension):
    snippets = models.ManyToManyField('Snippet')

    def copy_relations(self, oldinstance, language):
        for snippet in oldinstance.snippets.all():
            self.snippets.add(snippet)


extension_pool.register(SnippetExtension)


class Snippet(models.Model):
    code = models.TextField()
