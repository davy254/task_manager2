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



class Task(models.Model):
    """Task model"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Tasks"


    def __str__(self):
        return f'{self.title} - {"Completed" if self.is_completed else "Pending"}'

    def __repr__(self):
        return f'<Task(title={self.title}, is_completed={self.is_completed}, due_date={self.due_date})>'
    
