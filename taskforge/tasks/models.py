from django.db import models
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)


    class Meta:
        verbose_name_plural = "Projects"
        ordering =["-created_at"]

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<Project(name={self.name}, created_at={self.created_at}, slug={self.slug})>"


    def save(self, *args, **kwargs):
        # Regenerate slug  if name changes OR slug is empty
        if not self.slug or Project.objects.filter(name=self.name).exclude(id=self.id).exists():
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    