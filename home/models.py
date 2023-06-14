from django.db import models

class questions(models.Model):
    quest= models.TextField()
    code = models.TextField()
    
    def __str__(self):
        return self.code
