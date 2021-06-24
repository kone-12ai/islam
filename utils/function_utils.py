# utils.context_proc.py

import string
import random

from django.conf import settings
from django.utils.text import slugify


def taleeb_context_processor(request):
    return {
        'site_title': settings.SITE_NAME,
        'addr_email': 'taleebinfoO44@gmail.com',
        'addr_contact': '07 47 09 25 52',
        'developper': 'Taleeb Soft Technologie',
        'site_description': settings.SITE_DESCRIPTION,
        'site_keywords': settings.META_KEYWORDS,
        'request': request,
    }

def random_string_generator(size=8, carac=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(carac) for _ in range(size))

def unique_slug_generator(instance, slug=None):
    if slug is not None:
        slug = slug
    else:
        slug = slugify(instance.post_title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=8))
        return unique_slug_generator(instance, slug=slug)
    return slug

def unique_key_generator(instance):
    size = random.randint(20, 45)
    key = random_string_generator(size=size)
    Klass = instance.__class__
    qsx = Klass.objects.filter(key=key).exists()
    if qsx:
        return unique_slug_generator(instance)
    return key
