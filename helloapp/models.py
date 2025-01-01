from django.db import models

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'





class Book(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

