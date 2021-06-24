# blog.managers.py

# catalogue.managers.py

from django.db import models
from django.db.models import Q
from django.utils import timezone


class PostQuerySet(models.query.QuerySet):
    def posts_published(self):
        return self.filter(post_activated=True, post_status='PUBLISHED')

    def posts_drafted(self):
        return self.filter(post_status='DRAFT')

    def posts_sport(self):
        return self.filter(post_category='SPORT')

    def posts_religion(self):
        return self.filter(post_category='RELIGION')

    def posts_politique(self):
        return self.filter(post_category='POLITIQUE')

    def posts_communique(self):
        return self.filter(post_category='COMMUNIQUE')

    def posts_bouake_news(self):
        return self.filter(post_category='BOUAKE_NEWS')

    def posts_international(self):
        return self.filter(post_category='INTERNATIONAL')

    def posts_culture(self):
        return self.filter(post_category='SOCIETE_CULTURE')

    def post_recently(self):
        return self.filter(post_date_created__lte=timezone.now()).posts_published()

    def searching(self, query):
        lookups = (
            Q(post_title__icontains=query)
            | Q(post_category__icontains=query)
            | Q(post_content__icontains=query)
            | Q(post_keyword__icontains=query)
        )
        return self.filter(lookups).distinct()


class PostManager(models.Manager):

    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().posts_published()

    def sports(self):
        return self.get_queryset().posts_sport()

    def religion(self):
        return self.get_queryset().posts_religion()

    def culture(self):
        return self.get_queryset().posts_published()

    def bknews(self):
        return self.get_queryset().posts_bouake_news()

    def communique(self):
        return self.get_queryset().posts_communique()

    def politique(self):
        return self.get_queryset().posts_politique()

    def international(self):
        return self.get_queryset().posts_international()

    def post_recently(self, *args, **kwargs):
        return self.get_queryset().post_recently()

    def search(self):
        return self.get_queryset().product_recent_add().searching(query)

    def post_related(self, instance):
        post_ = self.get_queryset().filter(post_category=instance.post_category)
        post = (post_).exclude(id=instance.id).distinct()
        return post
