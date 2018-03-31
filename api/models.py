from django.db import models

# Create your models here.

class comment(models.Model):
    user = models.CharField(max_length = 30)
    text = models.TextField()

    def __str__(self):
        return "%s's comment" % (self.user)
