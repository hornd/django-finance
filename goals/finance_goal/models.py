from django.db import models

class Goal(models.Model):
    current_amount = models.IntegerField(default=0)
    goal_amount = models.IntegerField()
    end_date = models.DateTimeField('Due')
