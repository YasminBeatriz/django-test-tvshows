from django.db import models

class TVShow (models.Model):
    STATUS_TYPES = {
        ('1', 'Ongoing'),
        ('2', 'Finished'),
        ('3', 'Cancelled'),
    }
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=STATUS_TYPES)
    num_episodes = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)

    objects = models.Manager()
