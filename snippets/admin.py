from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import SnippetExtension, Snippet


class SnippetExtensionAdmin(PageExtensionAdmin):
    fields = ('name', 'snippets')
admin.site.register(SnippetExtension, SnippetExtensionAdmin)


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass
