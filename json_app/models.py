from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=200)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=100)
    
    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    
    def __str__(self):
        return str(self.user.real_name)