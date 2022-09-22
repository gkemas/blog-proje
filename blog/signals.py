from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post
from .utils import get_random_code

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):#kwarsgs arkada çalışan parametreleri bilmediğimiz için.
    if not instance.slug:
        instance.slug = slugify(instance.title + " " + get_random_code()) #sluıgify #strinlerin arasına boşluk koyuyor.


        