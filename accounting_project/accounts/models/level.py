from django.db import models

class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_title = models.CharField(max_length=100, default='No Title')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True)
    pre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.level_title} (ID: {self.level_id})"