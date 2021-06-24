# blog.admin.py

from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import Group

from blog.models import Post


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    model = Post
    date_hierarchy = 'post_date_created'
    fieldsets = (
        (
            'Article',
            {'fields': ('post_category', 'post_title', 'post_content', "post_cover", "post_keyword", 'post_status', 'post_activated',)}
        ),
        (
            'Analyse', {
                'classes': ('collapse',),
                'fields': ("post_viewed",)
            }
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty',),
            'fields': ('is_staff', 'is_active',)
        }),
    )
    list_per_page = 10
    ordering = ['-post_date_created']
    list_display_links = ['post_title']
    readonly_fields = ['post_url', 'post_viewed']
    search_fields = ["post_category", 'post_status']
    list_filter = ["post_category", "post_status", "post_activated"]
    list_editable = ["post_category", "post_status", "post_activated"]
    list_display = ["post_title", "post_category", "post_url", "post_status", "post_activated"]

    def post_url(self, instance):
        url = reverse('blog:post_detail', kwargs={
            'date': str(instance.post_date_created), 'slug': str(instance.slug), 'pk': int(instance.id)})
        response = format_html("""<a target='_blank' href="{0}">{0}</a>""", url)
        return response
    post_url.short_description = "Post URL"


admin.site.unregister(Group)
