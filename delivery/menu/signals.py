from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.cache import caches

from menu import models


@receiver(post_save, sender=models.Products)
def disabled_cache(sender, instance, **kwargs):
    c = caches[settings.CACHE_MIDDLEWARE_ALIAS]
    c.set(instance.get_absolute_url(), None)
    c.set(instance.category.get_absolute_url(), None)
