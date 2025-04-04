from django.db import models

class Project(models.Model):
    WORK_TYPES = [
        ("flooring", "Flooring"),
        ("electrical", "Electrical"),
        ("plumbing", "Plumbing"),
        ("carpentry", "Carpentry"),
        ("painting", "Painting"),
        ("roofing", "Roofing"),
        # Add more as needed
    ]

    type_of_work = models.CharField(max_length=50, choices=WORK_TYPES, default="flooring", null=True, blank=True)
    name = models.CharField(max_length=255, default=" ", null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='project_photos/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Photo for {self.project.name}"
