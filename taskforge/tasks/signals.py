from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Task
import uuid

@receiver(pre_save, sender=Task)
def set_task_slug(sender, instance, **kwargs):
    """
    Set a unique slug for the Task before saving.
    Regenerate slug if title changes or slug is empty.
    """
    if  not instance.slug or instance.slug =="":
        base_slug = slugify(instance.title)
        slug = base_slug
        counter = 1

        # Ensure slug is unique within the same project
        while Task.objects.filter(slug=slug, projectct=instance.project).exclude(pk=instance.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        instance.slug = slug
