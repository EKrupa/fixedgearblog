from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="Evan Krupa")
    image = models.ImageField(upload_to='media/images', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Gear(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"
    

class CommentMessage(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Bike(models.Model):
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.model   
    
