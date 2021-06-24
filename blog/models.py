# taleeb.models.py

import uuid
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.utils.text import Truncator

from utils import function_utils
from blog.managers import PostManager


class Post(models.Model):
    class PostStatus(models.TextChoices):
        DRAFT = "DRAFT", "Brouillon"
        PUBLISHED = "PUBLISHED", "Publier"

    default_status = PostStatus.DRAFT

    class PostCategory(models.TextChoices):
        SPORT = 'SPORT', 'Sport'
        RELIGION = "RELIGION", "Religion"
        POLITIQUE = "POLITIQUE", "Politique"
        COMMUNIQUE = "COMMUNIQUE", "Communiqué"
        BOUAKE_NEWS = "BOUAKE_NEWS", "Bouaké News"
        INTERNATIONAL = "INTERNATIONAL", "International"
        SOCIETE_CULTURE = "SOCIETE_CULTURE", "Société & Culture"

    default_category = PostCategory.RELIGION

    uuid = models.UUIDField(
        db_index=True, default=uuid.uuid4, editable=False, verbose_name='UUID'
    )
    post_category = models.CharField(
        default=default_category, choices=PostCategory.choices,
        verbose_name='post category', max_length=15
    )
    post_title = models.CharField(verbose_name='Titre du post', max_length=100)
    post_content = models.TextField(verbose_name='Contenu du post')
    post_keyword = models.CharField(max_length=100, verbose_name='mot cle')
    post_cover = models.ImageField(verbose_name='Importer image', upload_to='post/image/')
    post_viewed = models.PositiveIntegerField(verbose_name='post vu', default=0)
    post_activated = models.BooleanField(default=False, verbose_name='Activatez le post')
    post_date_created = models.DateField(auto_now=True, verbose_name='Post cree')
    post_status = models.CharField(
        default=default_status, choices=PostStatus.choices,
        max_length=9, verbose_name='Status du post'
    )
    slug = models.SlugField(verbose_name='Lien du post', unique=True)

    objects = PostManager()

    class Meta:
        db_table = 'post_title'
        ordering = ['-post_date_created']
        verbose_name_plural = 'Articles'
        indexes = [
            models.Index(fields=['id', 'uuid'], name='id_index')
        ]

    def __str__(self):
        return "{0}".format(self.post_title)

    def post_content_excerpt(self):
        truncated_post_content = Truncator(str(self.post_content))
        truncated_post_content_chars = truncated_post_content.words(14)
        return truncated_post_content_chars
    post_content_excerpt.short_description = 'Post content exercept'

    def post_get_lastest(self):
        post_latest = Post.objects.filter(post_created__lte=self.post_date_created)
        return post_latest

    def post_count(self):
        post_count = Post.objects.all().count()
        return post_count

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={
                'date': str(self.post_date_created),
                'slug': str(self.slug),
                'pk': int(self.id)
            }
        )

@receiver([models.signals.pre_save], sender=Post)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = function_utils.unique_slug_generator(instance)
