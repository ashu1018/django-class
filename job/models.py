from django.db import models
from django.contrib.auth.models import User

class Vacancy(models.Model):
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    image = models.ImageField(upload_to='vacancy')
    
    posted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-posted_at',)