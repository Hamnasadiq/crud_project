from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255, default='Unnamed Group', null=False)

    def __str__(self):
        return self.name