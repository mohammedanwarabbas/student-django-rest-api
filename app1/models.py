from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=50)
    s_age = models.IntegerField()
    s_gender = models.CharField(max_length=6)

    def __str__(self):
        return "{} - ({})".format(self.s_name,self.s_age)