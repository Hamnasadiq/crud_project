from django.db import models

class ChartOfAccount(models.Model):
    acc_id = models.IntegerField(primary_key=True)
    acc_name = models.CharField(max_length=100)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_name
