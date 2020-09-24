from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic th user is learning about"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE) #Since Django 2.x, on_delete is required.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."