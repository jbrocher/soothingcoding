from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class SnippetExtension(PageExtension):
    snippets = models.ManyToManyField('Snippet')



extension_pool.register(SnippetExtension)


class Snippet(models.Model):
    code = models.TextField()
