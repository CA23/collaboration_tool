from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    available_from = models.IntegerField()
    available_until = models.IntegerField()
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name + self.last_name + str(self.id)


    

