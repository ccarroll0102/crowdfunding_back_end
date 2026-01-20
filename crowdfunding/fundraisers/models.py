from django.db import models
#we are setting up our database models here and telling django what fields and what type of information for each field we want each model to have

# Create your models here.
class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonoymouns = models.BooleanField()
    fundraiser = models.ForeignKey('Fundraiser', on_delete=models.CASCADE, related_name='pledges')


