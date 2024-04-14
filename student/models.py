from django.db import models
class Students(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    KCPEmarks = models.IntegerField()
    age = models.IntegerField()

    class Meta:
              db_table = 'students'



