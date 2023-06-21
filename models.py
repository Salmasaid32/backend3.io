from django.db import models
class contact(models.model):
    title= models.charField(max_length=100)
    description = models.TextField()
    status= models.charField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=true)

    def __str__ (self):
        return self.title
