from django.contrib import admin

from .models import Note, Comment


admin.site.register(Note)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'note', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)