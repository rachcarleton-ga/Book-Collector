from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    publishedyear =  models.IntegerField()
    def __str__(self):
        return f'{self.title} ({self.id})'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    
class Reading(models.Model):
    date = models.DateField('reading date')
    time = models.CharField('reading duration', max_length=15)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.time} on {self.date}"

    class Meta:
        ordering =['-date']