from django.db import models

# Create your models here.


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_title = models.CharField(max_length=20)

    def __str__(self):
        return self.group_title


class Level(models.Model):
    lev_id = models.AutoField(primary_key=True)
    lev_title = models.CharField(max_length=50)
    pre_id = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.lev_title


class AccountMaster(models.Model):
    acc_id = models.AutoField(primary_key=True)
    acc_title = models.CharField(max_length=100)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_title
