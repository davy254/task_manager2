from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Projects"
        ordering =["-created_at"]

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<Project(name={self.name}, created_at={self.created_at})>"