from django.contrib import admin
from .models import Post, Contato


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'content', 'activated']
    search_fields = ['content']


"""
    def get_queryset(self, request):
        return Post.objects.filter(activated=True)
"""

admin.site.register(Post, PostAdmin)
admin.site.register(Contato)
